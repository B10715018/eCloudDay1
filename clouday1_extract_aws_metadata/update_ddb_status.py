import boto3
import datetime
import pytz

def update_ddb_status(requestID):
    client=boto3.client('dynamodb',region_name='us-west-2')
    date=datetime.datetime.now()
    # create taipei timezone
    tw=pytz.timezone('Asia/Taipei')
    twDate=tw.localize(date)
    client.update_item(TableName='architectureDB',
    Key={
        'requestID':{'S':requestID}
    },
    UpdateExpression="SET #attr1 = :var1, #attr2 = :var2",
    ExpressionAttributeNames={
        '#attr1': 'status',
        '#attr2':'timestamp',
    },
    ExpressionAttributeValues={
            ':var1': {'S':'UPDATING'},
            ':var2': {'S':str(twDate)},
            })