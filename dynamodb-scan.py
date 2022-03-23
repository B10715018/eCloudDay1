import boto3
import json

client=boto3.client('dynamodb')
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('translate')

response = table.scan()

existingKeys=[]

for item in response['Items']:
  for field in item.keys():
    if field not in existingKeys:
      existingKeys.append(field)

response['Items']=existingKeys
json_string=json.dumps(response)

with open ('./data/dynamoDB-item-list-scan.json','w') as outfile:
  outfile.write(json_string)