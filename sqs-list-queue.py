import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('sqs', region_name=REGION_NAME)

response = client.list_queues(
)

json_list = json.dumps(response)

with open('./data/sqs-list-queue'+'.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
