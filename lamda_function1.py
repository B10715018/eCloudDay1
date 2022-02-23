import boto3
import os
import uuid
# create lambda function if POST request is created
# function : to create a record in dynamoDB and publish SNS message
def lambda_handler(event, context):
    
    recordId = str(uuid.uuid4())
    url = event["url"]

    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('Input url: ' + url)
    
    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'url' : url,
            'status' : 'PROCESSING'
        }
    )
    
    #Sending notification about new post to SNS
    client = boto3.client('sns')
    client.publish(
        TopicArn = os.environ['SNS_TOPIC'],
        Message = recordId
    )
    
    return recordId
