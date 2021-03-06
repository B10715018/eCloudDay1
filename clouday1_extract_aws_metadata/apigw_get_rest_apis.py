import os
import boto3
from json import JSONEncoder
import datetime
import json
import os


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def apigw_get_rest_apis(region,AWS_ACCESS_KEY,AWS_SECRET_KEY):
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/apigw-get-rest-apis-'+region+'.json')

    client = boto3.client('apigateway', region_name=region,
    aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
    response = client.get_rest_apis()
    json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
    with open(file_path_write, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()

    return {
        'statusCode': 200,
    }
