import boto3
import os

# using server side encryption for the bucket make sure that data is encypted on transport and rest
def send_request_to_s3(account_name):
    script_dir=os.path.dirname('.')
    file_name=os.path.join(script_dir,'data/input.json')
    bucket_name='clouday1-userdata'
    object_name='user-'+account_name+'.json'
    client=boto3.client('s3',region_name='us-west-2')
    try:
        client.upload_file(file_name,bucket_name,object_name)
    except:
        print('Failed to export to S3')
