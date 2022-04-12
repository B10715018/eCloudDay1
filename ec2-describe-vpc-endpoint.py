import boto3
import json
import datetime
REGION_NAME = 'us-west-2'
client = boto3.client('ec2', region_name=REGION_NAME)
response = client.describe_vpc_endpoints()


def defaultconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


json_list = json.dumps(response, default=defaultconverter)
with open('./data/ec2-describe-vpc-endpoint.json', 'w') as outfile:
    outfile.write(json_list)
    outfile.close()
