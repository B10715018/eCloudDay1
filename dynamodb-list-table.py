import boto3
import json

client=boto3.client('dynamodb',region_name='us-west-2')
response = client.list_tables()
json_list=json.dumps(response)
with open('./data/dynamodb-list-table.json','w')as outfile:
  outfile.write(json_list)
  outfile.close()
