from ntpath import join
import boto3
import json

client=boto3.client('cloudtrail',region_name='us-west-2')
response = client.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'StartExecution'
        },
    ],
)

# count=0
# for items in response['Events']:
#     count+=1
#     eventList.append(json.dumps(items['EventTime'],default=str))

# for i in range(count):
#   response['Events'][i]['EventTime']=eventList[i]

for items in response['Events']:
    eventId=items['EventId']
    json_list=items['CloudTrailEvent']
    with open('./data/cloudtrail-lookup-event'+eventId+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()