import boto3
import json

client=boto3.client('ec2',region_name='us-west-2')
response = client.describe_route_tables()
json_list=json.dumps(response)
with open('./data/ec2-describe-route-table.json','w') as outfile:
  outfile.write(json_list)
  outfile.close()
