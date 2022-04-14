import os
import boto3
from json import JSONEncoder
import datetime
import json

REGION_NAME = 'us-west-2'

# subclass JSONEncoder


def apigw_get_resource():
    client = boto3.client('apigateway', region_name=REGION_NAME)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/apigw-get-rest-apis.json')
        f = open(file_path, 'r')
        data = json.load(f)
        count = 0
        ID = []
        for item in data['items']:
            count += 1
            ID.append(item['id'])

        class DateTimeEncoder(JSONEncoder):
            # Override the default method
            def default(self, obj):
                if isinstance(obj, (datetime.date, datetime.datetime)):
                    return obj.isoformat()

        for i in range(count):
            response = client.get_resources(
                restApiId=ID[i]
            )

            json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
            file_path2 = os.path.join(
                    script_dir, 'data/apigw-get-resource-'+ID[i]+'.json')
            with open(file_path2, 'w') as outfile:
                outfile.write(json_response)
                outfile.close()
    except:
        print('File not found for apigw-get-resources')
