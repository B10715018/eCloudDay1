import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('logs', region_name=REGION_NAME)
try:
    f = open('./data/cloudwatch-describe-log-groups.json')
    data = json.load(f)
    count = 0
    logGroupNameList = []
    for item in data['logGroups']:
        count += 1
        logGroupNameList.append(item['logGroupName'])

    for i in range(count):
        response = client.describe_log_streams(
            logGroupName=logGroupNameList[i],
            orderBy='LastEventTime',
            limit=1
            )
        json_list = json.dumps(response)

        str_logGroupName = "".join(logGroupNameList[i])
        new_logGroupName = str_logGroupName.replace('/', '-')
        list(new_logGroupName)

        with open('./data/cloudwatch-log-stream/cloudwatch-describe-log-stream'+new_logGroupName+'.json', 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
except:
    print("File not found for cloudwatch-describe-log-stream")

    

