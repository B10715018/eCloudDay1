import os
import boto3
import json
REGION_NAME = 'us-west-2'


def cloudwatch_describe_log_event():
    client = boto3.client('logs', region_name=REGION_NAME)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(
        script_dir, 'data/cloudwatch-describe-log-groups.json')
    f = open(file_path, 'r')
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
        file_path2 = os.path.join(
            script_dir, 'data/cloudwatch-log-stream/cloudwatch-describe-log-stream' +
            new_logGroupName+'.json''
        )
        a = open(file_path2, 'r')
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
                file_path3 = os.path.join(
                    script_dir, 'data/cloudwatch-log-stream/cloudwatch-get-log-event'+new_logStreamName+'.json')
                with open(file_path3, 'w')as outfile:
                    outfile.write(json_list)
                    outfile.close()
        except:
            print("logStreams not found")
