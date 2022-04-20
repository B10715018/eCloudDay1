import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('ec2', region_name=REGION_NAME)
response = client.describe_subnets()
json_list = json.dumps(response)
with open('./data/ec2-describe-subnet.json', 'w') as outfile:
    outfile.write(json_list)
    outfile.close()