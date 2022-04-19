import boto3
import json
import os
# describe available state machine
REGION_NAME = 'us-west-2'
client = boto3.client('stepfunctions', region_name=REGION_NAME)
# describe all available state machine

def sfn_describe():

    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/step-function-list-state-machine.json')
        f = open(file_path, 'r')
        data = json.load(f)

        count = 0
        stateARN = []
        for items in data['stateMachines']:
            count += 1
            stateARN.append(items['stateMachineArn'])

        for i in range(count):
            response2 = client.describe_state_machine(
                stateMachineArn=stateARN[i])
            definition = response2['definition']
            response2.pop('definition')
            serializeDate = json.dumps(response2['creationDate'], default=str)
            response2['creationDate'] = serializeDate
            json_string = json.dumps(response2)

            #use os path
            filename = os.path.join(
            script_dir, 'data/sfn-describe-'+stateARN[i]+'-policy.json')
            filename2 = os.path.join(
            script_dir, 'data/sfn-definition-'+stateARN[i]+'-policy.json')

            with open(filename, 'w') as outfile:
                outfile.write(json_string)
                outfile.close()

            with open(filename2, 'w') as outfile2:
                outfile2.write(definition)
                outfile2.close()
    except:
        print('File not found for sfn-describe')
