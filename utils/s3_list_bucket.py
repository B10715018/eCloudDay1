import boto3
from json import JSONEncoder
import datetime
import json
import os

REGION_NAME = 'us-west-2'

def s3_list_bucket():
    client = boto3.client('s3', region_name=REGION_NAME)
   
    # subclass JSONEncoder
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


    response = client.list_buckets()
    json_response= json.dumps(response, indent=4, cls=DateTimeEncoder)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/s3-list-bucket.json')
    with open(file_path, 'w') as outfile:
        outfile.write(json_response)
        outfile.close()

