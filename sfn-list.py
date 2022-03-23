
import boto3
import json
# list available state machine
client=boto3.client('stepfunctions',region_name='us-west-2')
response=client.list_state_machines()


sfnList=[]
count=0
for item in response['stateMachines']:
  count+=1
  sfnList.append(json.dumps(item['creationDate'],default=str))
  print(sfnList)

for i in range(count):
  response['stateMachines'][i]['creationDate']=sfnList[i]

json_string_list=json.dumps(response)



with open('./data/step-function-list-state-machine.json','w')as outfile:
  outfile.write(json_string_list)
  outfile.close()
