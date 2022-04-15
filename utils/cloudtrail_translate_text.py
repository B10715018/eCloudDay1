import boto3
from json import JSONEncoder
import datetime
import json
import ast

# subclass JSONEncoder
REGION_NAME='us-west-2'

def cloudtrail_translate_text():
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    try:
        client = boto3.client('cloudtrail', region_name=REGION_NAME)
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
        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/cloudtrail-translate-text.json')
        with open(file_path,'w') as outfile:
            outfile.write(json_list)
            outfile.close()

        # make json file only out of the cloud trail event
        eventId = response['Events'][0]['EventId']
        json_list_cloudtrail = response['Events'][0]['CloudTrailEvent']
        file_path2 = os.path.join(script_dir,'data/cloudtrail-translate-text-'+eventId+'.json')
        with open(file_path2, 'w')as outfile:
            outfile.write(json_list_cloudtrail)
            outfile.close()

        # take the user agent value to judge whether or not instance is lambda/ ec2 instance
        json_list_cloudtrail = json.loads(json_list_cloudtrail)
        if('Lambda' in json_list_cloudtrail['userAgent']):
            print('Lambda is found')
    except:
        print('File not found for cloudtrail-translate-text')