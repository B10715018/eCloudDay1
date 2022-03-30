import boto3
import json

client=boto3.client('rds',region_name='us-west-2')
response =client.describe_db_instances()
json_list=json.dumps(response)
with open('./data/rds-describe-instance.json','w') as outfile:
  outfile.write(json_list)
  outfile.close()
