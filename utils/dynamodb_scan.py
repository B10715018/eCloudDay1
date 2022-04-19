import boto3
import json
import os

REGION_NAME = 'us-west-2'


def dynamodb_scan():
    client = boto3.client('dynamodb', region_name=REGION_NAME)
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
    count = 0
    TableList = []
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/dynamodb-list-table.json')
    f = open(file_path, 'r')
    data = json.load(f)
    for item in data['TableNames']:
        count+=1
        TableList.append(item)
    try:
        for i in range(count):
            table=dynamodb.Table(TableList[i])
            response = table.scan()

            existingKeys = []

        for items in response['Items']:
            for field in items.keys():
                if field not in existingKeys:
                    existingKeys.append(field)

        response['Items'] = existingKeys
        json_string = json.dumps(response)
        file_path2=os.path.join(script_dir,'data/dynamoDB-item-list-scan-'+TableList[i]+'.json')
        with open(file_path2, 'w') as outfile:
            outfile.write(json_string)
            outfile.close()
    except:
        print('File not found for dynamodb scan')

