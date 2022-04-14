import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('logs', region_name=REGION_NAME)
f = open('./data/cloudwatch-describe-log-groups.json')
data = json.load(f)
count = 0
countStream = 0
logGroupNameList = []
LogStreamNameList = []

for item in data['logGroups']:
    count += 1
    logGroupNameList.append(item['logGroupName'])
    
for i in range(count):
    str_logGroupName = "".join(logGroupNameList[i])
    new_logGroupName = str_logGroupName.replace('/', '-')
    list(new_logGroupName)
    a = open('./data/cloudwatch-log-stream/cloudwatch-describe-log-stream' +
             new_logGroupName+'.json', 'r')
    logs = json.load(a)
    a.close()
    try:
        for Stream in logs['logStreams']:
            countStream += 1
            LogStreamNameList.append(Stream['logStreamName'])
            str_logStreamName = "".join(LogStreamNameList[i])
            new_logStreamName = str_logStreamName.replace('/', '-')
            response = client.get_log_events(
                logGroupName=logGroupNameList[i],
                logStreamName=str_logStreamName
            )
            json_list = json.dumps(response)
            with open('./data/cloudwatch-log-stream/cloudwatch-get-log-event'+new_logStreamName+'.json', 'w')as outfile:
                outfile.write(json_list)
                outfile.close()
    except:
        print("logStreams not found")
