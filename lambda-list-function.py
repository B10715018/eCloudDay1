
import boto3
import json

client=boto3.client('lambda',region_name='us-west-2')
response=client.list_functions()
json_list=json.dumps(response)
#print(json_list)

with open('./data/lambda-list-functions.json','w')as outfile:
  outfile.write(json_list)
  outfile.close()
