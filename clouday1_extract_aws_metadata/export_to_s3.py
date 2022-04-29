import boto3
import os
import uuid
import datetime

object_name='data-'+str(uuid.uuid4())+'.json'

def upload_to_S3(region):
    script_dir=os.path.dirname('.')
    file_name=os.path.join(script_dir,'data/data.json')
    bucket_name='clouday1-metadata'

    client=boto3.client('s3',region_name=region)
    try:
        client.upload_file(file_name,bucket_name,object_name)
    except:
        print('Failed to export to S3')


def write_to_dynamo_db(region,account_id):
    client=boto3.client('dynamodb',region_name=region)
    item_dict={
        'account_id':{'S':account_id},
        'status': {'S':'COMPLETED'},
        'data_name': {'S':object_name},
        'timestamp': {'S':str(datetime.datetime.now())}
    }
    client.put_item(TableName='architecture',
    Item=item_dict)
