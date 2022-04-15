import boto3
from json import JSONEncoder
import datetime
import json
import os
# subclass JSONEncoder
REGION_NAME = 'us-west-2'


def ec2_describe_instances():
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    client = boto3.client('ec2', region_name=REGION_NAME)
    response = client.describe_instances()

    response2 = json.dumps(response, indent=4, cls=DateTimeEncoder)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/ec2-describe-instances.json')
    with open(file_path, 'w')as outfile:
        outfile.write(response2)
        outfile.close()
        
    return{
        'statusCode': 200
    }
