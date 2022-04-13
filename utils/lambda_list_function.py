import os
import boto3
import json

REGION_NAME = 'us-west-2'


def lambda_list_function():
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/lambda-list-functions.json')
    client = boto3.client('lambda', region_name=REGION_NAME)
    response = client.list_functions()
    json_list = json.dumps(response)

    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()

    return {
        'statusCode': 200,
    }
