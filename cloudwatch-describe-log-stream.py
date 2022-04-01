import boto3
import json
client = boto3.client('logs', region_name='us-west-2')
response = client.describe_log_streams(
    logGroupName='aws-cloudtrail-logs-758325631830-df00f960',
)
json_list = json.dumps(response)
# print(json_list)

with open('./data/cloudwatch-get-log-streams.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
