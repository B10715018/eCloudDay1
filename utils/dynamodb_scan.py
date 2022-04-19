import os
import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('dynamodb', region_name=REGION_NAME)
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


def dynamodb_scan():
    
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/dynamodb-list-table.json')
    f = open(file_path, 'r')
    data = json.load(f)
    count = 0
    tableNameList = []

    for i in data['TableNames']:
        count += 1
        tableNameList.append(i)

    for k in range(count):
        table = dynamodb.Table(tableNameList[k])
        response = table.scan()


        existingKeys = []
        for item in response['Items']:
            for field in item.keys():
                if field not in existingKeys:
                    existingKeys.append(field)

        response['Items'] = existingKeys
        json_response = json.dumps(response)

        file_path2 = os.path.join(script_dir, 'data/dynamodb-'+tableNameList[k]+'-scan.json')
        with open(file_path2, 'w') as outfile:
            outfile.write(json_response)
            outfile.close()
