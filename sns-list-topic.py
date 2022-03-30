import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('sns', region_name=REGION_NAME)

response = client.list_topics()

json_list = json.dumps(response)

with open('./data/sns-list-topic-'+REGION_NAME+'.json', 'w') as outfile:
    outfile.write(json_list)
    outfile.close()
