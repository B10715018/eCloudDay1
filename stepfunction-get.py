from urllib import response
import boto3
import json

client=boto3.client('stepfunctions',region_name='us-west-2')
response=client.list_state_machines()
print(response)
for item in response['stateMachines']:
  print(response['stateMachines'])
  response['stateMachines'][item].append(json.dumps(item['creationDate'],default=str))
json_string_list=json.dumps(response)

response2=client.describe_state_machine(
  stateMachineArn='arn:aws:states:us-west-2:758325631830:stateMachine:lambda'
)

definition=response2['definition']
response2.pop('definition')
serializeDate=json.dumps(response2['creationDate'],default=str)
response2['creationDate']=serializeDate
json_string=json.dumps(response2)

with open('./data/step-function-list-state-machine.json','w')as outfile:
  outfile.write(json_string_list)
  outfile.close()

with open('./data/step-function-describe-state-machine.json','w') as outfile:
  outfile.write(json_string)
  outfile.close()

with open('./data/step-function-definition.json','w') as outfile2:
  outfile2.write(definition)
  outfile2.close()