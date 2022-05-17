import boto3
import os
import json

def get_credentials_from_s3(account_name):
    try:
        # download the credential file
        script_dir=os.path.dirname('.')
        file_name=os.path.join(script_dir,'data/credentials.json')
        client=boto3.client('s3',region_name='us-west-2')
        object_name='user-'+account_name+'.json'
        client.download_file('clouday1-userdata',object_name,file_name)
        with open(file_name,'r') as openfile:
            json_object=json.load(openfile)
            openfile.close()
    except:
        return {
            'status': 'Error',
            'code': 500,
            'message': 'Bad Error Request'
        }
    return {
        'status': 'Success',
        'code': 200,
        'message':json_object
        }
