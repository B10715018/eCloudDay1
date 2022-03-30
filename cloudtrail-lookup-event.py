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


client = boto3.client('cloudtrail', region_name='us-west-2')
response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'StartExecution'
        },
    ],
    MaxResults=1,
)

# this is only for cloud trail events only
for items in response['Events']:
    eventId = items['EventId']
    json_list = items['CloudTrailEvent']
    with open('./data/cloudtrail-lookup-event-'+eventId+'.json', 'w')as outfile:
        outfile.write(json_list)
        outfile.close()

# this is for the whole event

json_list2 = json.dumps(response, indent=4, cls=DateTimeEncoder)
with open('./data/cloudtrail-lookup-event'+'.json', 'w')as outfile:
    outfile.write(json_list2)
    outfile.close()
