import boto3
import json
import os

REGION_NAME = 'us-west-2'


def lambda_get_policy():
    client = boto3.client('lambda', region_name=REGION_NAME)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/lambda-list-functions.json')
        f = open(file_path, 'r')
        data = json.load(f)
        count = 0
        lambdaNameList = []
        for item in data['Functions']:
            count += 1
            lambdaNameList.append(item['FunctionArn'])
        for i in range(count):
            try:
                response = client.get_policy(
                    FunctionName=lambdaNameList[i]
                )
                json_response = json.dumps(response)
                file_path2 = os.path.join(
                    script_dir, 'data/lambda-'+lambdaNameList[i]+'-policy.json')
                with open(file_path2, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()
            except:
                print('Error in getPolicy')

    except:
        print('File not found for lambda-get-policy')
