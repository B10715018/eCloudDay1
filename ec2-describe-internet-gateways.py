import boto3
import json

client = boto3.client('ec2', region_name='us-west-2')
response = client.describe_internet_gateways()

# print(response)
json_list = json.dumps(response , indent=4)
with open('./data/ec2-describe-internet-gateways.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()