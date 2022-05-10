import boto3
import datetime

def initial_request_to_ddb(region,account_id):
    client=boto3.client('dynamodb',region_name='us-west-2')
    item_dict={
        'account_id':{'S':account_id},
        'status': {'S':'PROCESSING'},
        'region': {'SS':region},
        'timestamp': {'S':str(datetime.datetime.now())}
    }
    client.put_item(TableName='architecture',
    Item=item_dict)
