import boto3
import json
import os
REGION_NAME = 'us-west-2'


def ec2_describe_subents():
    client = boto3.client('ec2', region_name=REGION_NAME)
    response = client.describe_subnets()
    json_list = json.dumps(response)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/ec2-describe-subnet.json')
    with open(file_path, 'w') as outfile:
        outfile.write(json_list)
        outfile.close()
