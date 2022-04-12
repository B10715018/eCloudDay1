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
client = boto3.client('ec2', region_name=REGION_NAME)
response = client.describe_availability_zones()

# print(response)
json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
with open('./data/ec2-describe-availability-zones.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
