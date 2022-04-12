
import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('lambda', region_name=REGION_NAME)
response = client.list_functions()
json_list = json.dumps(response)


with open('./data/lambda-list-functions.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
