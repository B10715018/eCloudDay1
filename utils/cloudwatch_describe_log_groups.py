import os
import boto3
import json
REGION_NAME = 'us-west-2'


def cloudwatch_describe_log_groups():
    client = boto3.client('logs', region_name=REGION_NAME)
    response = client.describe_log_groups()
    json_list = json.dumps(response)

    script_dir = os.path.dirname('.')
    file_path = os.path.join(
        script_dir, './data/cloudwatch-describe-log-groups.json')

    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()
