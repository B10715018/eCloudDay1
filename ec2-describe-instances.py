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


client = boto3.client('ec2', region_name='us-west-2')
response = client.describe_instances(
    InstanceIds=[
        'i-04850a0016b6718f2',
        'i-08e41dc2ea3da1a9f'
    ],
)


response2 = json.dumps(response, indent=4, cls=DateTimeEncoder)

with open('./data/ec2-describe-instances'+'.json', 'w')as outfile:
    outfile.write(response2)
    outfile.close()
