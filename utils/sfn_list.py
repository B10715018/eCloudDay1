import boto3
import json
import os
# list available state machine
REGION_NAME = 'us-west-2'
client = boto3.client('stepfunctions', region_name=REGION_NAME)

def sfn_list():
    
    response = client.list_state_machines()
    sfnList = []
    count = 0
    for item in response['stateMachines']:
        count += 1
        sfnList.append(json.dumps(item['creationDate'], default=str))


    for i in range(count):
        response['stateMachines'][i]['creationDate'] = sfnList[i]

    json_string_list = json.dumps(response)

    script_dir = os.path.dirname('.')
    file_path = os.path.join(
        script_dir, 'data/step-function-list-state-machine.json')
    with open(file_path, 'w')as outfile:
        outfile.write(json_string_list)
        outfile.close()
