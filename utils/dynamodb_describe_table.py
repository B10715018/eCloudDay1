import os
import boto3
import json
from json import JSONEncoder
import datetime

REGION_NAME = 'us-west-2'


def dynamodb_describe_table():
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    client = boto3.client('dynamodb', region_name=REGION_NAME)
    TableNameList = []
    count = 0
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/dynamodb-list-table.json')
    f = open(file_path, 'r')
    data = json.load(f)

    for item in data['TableNames']:
        TableNameList.append(item)
        count += 1
    for i in range(count):
        response = client.describe_table(
            TableName=TableNameList[i]
        )
        json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
        file_path2 = os.path.join(
            script_dir, 'data/dynamodb-describe-table-'+TableNameList[i]+'.json')
        with open(file_path2, 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
