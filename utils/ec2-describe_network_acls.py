import boto3
import json
import os
REGION_NAME = 'us-west-2'


def describe_network_acls():
    client = boto3.client('ec2', region_name=REGION_NAME)
    response = client.describe_network_acls()

    json_list = json.dumps(response, indent=4)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/ec2-describe-network-acls.json')
    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()
