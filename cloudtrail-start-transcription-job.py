import boto3

client=boto3.client('cloudtrail',region_name='us-west-2')
response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'StartTranscriptionJob'
        },
    ],
    MaxResults=1
)
for items in response['Events']:
    eventId=items['EventId']
    json_list=items['CloudTrailEvent']
    with open('./data/cloudtrail-start-transcription-job-'+eventId+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()