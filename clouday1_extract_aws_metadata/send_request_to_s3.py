import boto3
import os
import json

# using server side encryption for the bucket make sure that data is encypted on transport and rest
def send_request_to_s3(account_name,account_id,aws_access_key_id,aws_secret_access_key,
regions,userId,aws_session_token):
    credentials={
        'account_name':account_name,
        'account_id':account_id,
        'user_id':userId,
        'region':regions,
        'aws_access_key_id':aws_access_key_id,
        'aws_secret_access_key':aws_secret_access_key,
        'aws_session_token':aws_session_token
    }
    script_dir=os.path.dirname('.')
    file_name=os.path.join(script_dir,'data/input.json')
    with open(file_name,'w') as outfile:
        outfile.write(json.dumps(credentials))
    bucket_name='clouday1-userdata'
    object_name='user-'+account_name+'.json'
    client=boto3.client('s3',region_name='us-west-2')
    try:
        client.upload_file(file_name,bucket_name,object_name)
    except:
        print('Failed to export to S3')
