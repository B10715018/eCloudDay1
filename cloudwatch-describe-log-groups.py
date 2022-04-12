import boto3
import json
REGION_NAME = 'us-west-2'
client=boto3.client('logs',region_name=REGION_NAME)
response = client.describe_log_groups()
json_list = json.dumps(response)

with open('./data/cloudwatch-describe-log-groups.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
