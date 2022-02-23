import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
 # lambda function that will fetch text variable from the DynamoDB and later translate the text and publish SNS topic to trigger lambda_function4.py
def lambda_handler(event, context):
    
    postId = event["postId"]
    sourceLanguage=event["sourceLang"]
    targetLanguage=event["targetLang"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    
    if postId=="*":
        items = table.scan()
    else:
        items = table.query(
            KeyConditionExpression=Key('id').eq(postId)
        )
    
    translate = boto3.client(service_name='translate', region_name='eu-west-1', use_ssl=True)

    result = translate.translate_text(Text=items["Items"][0]["text"], 
            SourceLanguageCode=sourceLanguage, TargetLanguageCode=targetLanguage)
    print('TranslatedText: ' + result.get('TranslatedText'))
    print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
    print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
    
    response = table.update_item(
                Key={'id':postId},
                  UpdateExpression=
                    "SET #statusAtt = :statusValue, #urlAtt = :urlValue",                   
                  ExpressionAttributeValues=
                    {':statusValue': 'UPDATED 2', ':urlValue': result.get('TranslatedText')},
                ExpressionAttributeNames=
                  {'#statusAtt': 'status', '#urlAtt': 'translatedText'},
            )
    
   #Sending notification about new post to SNS
    client = boto3.client('sns')
    client.publish(
        TopicArn = os.environ['SNS_TOPIC'],
        Message = postId
    )
    
    return items["Items"]