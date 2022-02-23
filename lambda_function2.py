import boto3
import os
import uuid
import json
from boto3.dynamodb.conditions import Key,Attr
import time
# this lambda function is triggered when SNS from lambda_function1.py is published
# function: convert audio taken from s3 and convert to text using Transcribe
def lambda_handler(event, context):

    postId = event["Records"][0]["Sns"]["Message"]
    
    print ("Text to Speech function. Post ID in DynamoDB: " + postId)
    
    #Retrieving information about the post from DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    postItem = table.query(
        KeyConditionExpression=Key('id').eq(postId)
    )
    

    url = postItem["Items"][0]["url"]
    
    s3Path = url
    jobName = 'job' + '-' + str(uuid.uuid4())

    client = boto3.client('transcribe')

    response = client.start_transcription_job(
        TranscriptionJobName=jobName,
        LanguageCode='zh-TW',
        MediaFormat='mp4',
        Media={
            'MediaFileUri': s3Path
        },
        OutputBucketName = os.environ['BUCKET_NAME']
    )
    
    while True:
        result=client.get_transcription_job(TranscriptionJobName=jobName)
        if result['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            print(result['TranscriptionJob']['TranscriptionJobStatus'])
            break
        time.sleep(5)
    if result['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
            s3 = boto3.resource('s3')
            content_object = s3.Object(os.environ['BUCKET_NAME'], jobName+".json")
            file_content = content_object.get()['Body'].read().decode('utf-8')
            json_content = json.loads(file_content)
            datas=json_content['results']['transcripts'][0]['transcript']
            response = table.update_item(
                Key={'id':postId},
                  UpdateExpression=
                    "SET #statusAtt = :statusValue, #urlAtt = :urlValue",                   
                  ExpressionAttributeValues=
                    {':statusValue': 'UPDATED', ':urlValue': datas},
                ExpressionAttributeNames=
                  {'#statusAtt': 'status', '#urlAtt': 'text'},
            )
        
            

    return 