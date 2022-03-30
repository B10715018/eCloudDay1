import boto3
from json import JSONEncoder
import datetime
import json
import ast

# subclass JSONEncoder


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


client = boto3.client('cloudtrail', region_name='us-west-2')
response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'TranslateText'
        },
    ],
    MaxResults=1,
)
# encode the whole event to json file
json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
with open('./data/cloudtrail-translate-text'+'.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()

# make json file only out of the cloud trail event
eventId = response['Events'][0]['EventId']
json_list_cloudtrail = response['Events'][0]['CloudTrailEvent']
with open('./data/cloudtrail-translate-text-'+eventId+'.json', 'w')as outfile:
    outfile.write(json_list_cloudtrail)
    outfile.close()

# take the user agent value to judge whether or not instance is lambda/ ec2 instance
json_list_cloudtrail = json.loads(json_list_cloudtrail)
if('Lambda' in json_list_cloudtrail['userAgent']):
    print('Lambda is found')
