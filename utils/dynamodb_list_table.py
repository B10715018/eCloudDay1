import boto3
import json
import os

REGION_NAME = 'us-west-2'

def dynamodb_list_table():
    client = boto3.client('dynamodb', region_name=REGION_NAME)
    try:
        script_dir = os.path.dirname('.')
        response = client.list_tables()
        json_response = json.dumps(response)
        file_path = os.path.join(
        script_dir, 'data/dynamodb-list.json')
        with open(file_path, 'w') as outfile:
            outfile.write(json_response)
            outfile.close()
 

    except:
        print('File not found for dynamodb-list-table')
