import json
import boto3

client=boto3.client('cloudtrail',region_name='us-west-2')
response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'TranslateText'
        },
    ],
    MaxResults=1,
)
# print(response['Events'])
for items in response['Events']:
    eventId=items['EventId']
    json_list=items['CloudTrailEvent']
    print(json_list['userAgent'])
    with open('./data/cloudtrail-translate-text-'+eventId+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()