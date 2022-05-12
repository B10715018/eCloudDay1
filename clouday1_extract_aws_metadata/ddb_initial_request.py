import boto3
import datetime
import uuid

def initial_request_to_ddb(region,account_id,account_name,user_id):
    client=boto3.client('dynamodb',region_name='us-west-2')
    requestId=str(uuid.uuid4())
    item_dict={
        'requestID': {'S':requestId},
        'account_id':{'S':account_id},
        'account_name':{'S': account_name},
        'user_id': {'S': user_id},
        'data_name':{'S':''},
        'status': {'S':'PROCESSING'},
        'region': {'SS':region},
        'timestamp': {'S':str(datetime.datetime.now())}
    }
    client.put_item(TableName='architectureDB',
    Item=item_dict)
    return requestId