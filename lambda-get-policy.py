import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('lambda', region_name=REGION_NAME)
try:
    f = open('./data/lambda-list-functions.json')
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
            filename = './data/lambda-'+lambdaNameList[i]+'-policy.json'
            with open(filename, 'w') as outfile:
                outfile.write(json_response)
                outfile.close()
        except:
            print('Error in getPolicy')

except:
    print('File not found for lambda-get-policy')
