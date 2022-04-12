import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('ec2', region_name=REGION_NAME)
response = client.describe_internet_gateways()

# print(response)
json_list = json.dumps(response, indent=4)
with open('./data/ec2-describe-internet-gateways.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
