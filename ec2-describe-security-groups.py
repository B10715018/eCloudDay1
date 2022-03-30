import boto3
import json

client=boto3.client('ec2',region_name='us-west-2')
response = client.describe_security_groups()
#print(response)
json_list=json.dumps(response)
with open('./data/ec2-describe-security-groups.json','w')as outfile:
  outfile.write(json_list)
  outfile.close()