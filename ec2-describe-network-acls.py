import boto3
import json

client = boto3.client('ec2', region_name='us-west-2')
response = client.describe_network_acls()

# print(response)
json_list = json.dumps(response , indent=4)
with open('./data/ec2-describe-network-acls.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()