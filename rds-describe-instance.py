import boto3
import json

REGION_NAME = 'us-west-2'
client=boto3.client('rds',region_name=REGION_NAME)
response =client.describe_db_instances()
json_list=json.dumps(response)
with open('./data/rds-describe-instance.json','w') as outfile:
  outfile.write(json_list)
  outfile.close()
