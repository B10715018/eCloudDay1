import boto3
import json

client = boto3.client('logs', region_name='us-west-2')
f = open('./data/cloudwatch-get-log-streams.json')
data = json.load(f)
count = 0
LogStreamName = []
all_event=[]
for item in data['logStreams']:
    count += 1
    LogStreamName.append(item['logStreamName'])
    # print(LogStreamName)
for i in range(count):
    response = client.get_log_events(
        logGroupName='aws-cloudtrail-logs-758325631830-2cc34dd3',
        logStreamName=LogStreamName[i]
    )
    json_list = json.dumps(response)
    # print(json_list)
    all_event.append(json_list)
    all_event_json=json.dumps(all_event,indent=4, sort_keys=True)
    with open('./data/cloudwatch-'+LogStreamName[i]+'-get-log-events.json', 'w')as outfile:
        outfile.write(json_list)
        outfile.close()
with open('./data/cloudwatch-get-log-events-all.json', 'w')as outfile:
        outfile.write(all_event_json)
        outfile.close()