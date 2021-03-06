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


def s3_list_bucket(region,AWS_ACCESS_KEY,AWS_SECRET_KEY):
    client = boto3.client('s3', region_name=region,
    aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)

    response = client.list_buckets()
    json_response = json.dumps(response, indent=4, cls=DateTimeEncoder)
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/s3-list-bucket-'+region+'.json')
    with open(file_path_write, 'w') as outfile:
        outfile.write(json_response)
        outfile.close()
