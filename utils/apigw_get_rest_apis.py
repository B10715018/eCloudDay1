import os
import boto3
from json import JSONEncoder
import datetime
import json

# subclass JSONEncoder
REGION_NAME = 'us-west-2'


def apigw_get_rest_apis():
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/lapigw-get-rest-apis'+'.json')

    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    client = boto3.client('apigateway', region_name=REGION_NAME)
    response = client.get_rest_apis()
    json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()

    return {
        'statusCode': 200,
    }
 # test
