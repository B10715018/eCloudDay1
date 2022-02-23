import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
# this lambda function is triggered when SNS Topic from lambda_function3.py is published for translation message
# function : to return the parameter of the record in dynamoDB
def lambda_handler(event, context):
    
    postId = event["Records"][0]["Sns"]["Message"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    
    if postId=="*":
        items = table.scan()
    else:
        items = table.query(
            KeyConditionExpression=Key('id').eq(postId)
        )
    
    return items["Items"]