import os
import boto3
from json import JSONEncoder
import datetime
import json

# subclass JSONEncoder
REGION_NAME = 'us-west-2'


def cloudtrail_lookup_event():
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(
            script_dir, 'data/cloudtrail-lookup-event-'+eventId+'.json')
        file_path2 = os.path.join(
            script_dir, 'data/cloudtrail-lookup-event.json')
        client = boto3.client('cloudtrail', region_name=REGION_NAME')
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
            with open(file_path, 'w')as outfile:
                outfile.write(json_list)
                outfile.close()

    # this is for the whole event

        json_list2 = json.dumps(response, indent=4, cls=DateTimeEncoder)
        with open(file_path2, 'w')as outfile2:
            outfile2.write(json_list2)
            outfile2.close()
    except:
        print('File not found for cloudtrail_lookup_event')
