import boto3
import json
import datetime
import os
REGION_NAME = 'us-west-2'


def ec2_describe_vpc_endpoint():
    client = boto3.client('ec2', region_name=REGION_NAME)
    response = client.describe_vpc_endpoints()

    def defaultconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    json_list = json.dumps(response, default=defaultconverter)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/ec2-describe-vpc-endpoint.json')
    with open(file_path, 'w') as outfile:
        outfile.write(json_list)
        outfile.close()
