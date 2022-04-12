import boto3
from json import JSONEncoder
import datetime
import json

# subclass JSONEncoder


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


REGION_NAME = 'us-west-2'
client = boto3.client('ec2', region_name=REGION_NAME')
response = client.describe_instances()


response2 = json.dumps(response, indent=4, cls=DateTimeEncoder)

with open('./data/ec2-describe-instances'+'.json', 'w')as outfile:
    outfile.write(response2)
    outfile.close()
