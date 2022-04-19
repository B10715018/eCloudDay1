import json
import boto3
import os

REGION_NAME = 'us-west-2'


def cloudtrail_waf_createWEBACL():
    client = boto3.client('cloudtrail', region_name=REGION_NAME)

    response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventName',
                'AttributeValue': 'CreateWebACL'
            },
        ],
        MaxResults=1,
    )
    for items in response['Events']:
        eventId = items['EventId']
        json_list = items['CloudTrailEvent']
        script_dir = os.path.dirname('.')
        file_path = (
            script_dir, 'data/cloudtrail-waf-createWebACL-'+eventId+'.json')
        with open(file_path, 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
