import json
import boto3
import os

client = boto3.client('wafv2', region_name='us-west-2')
response = client.get_web_acl(
    Name='wafELB',
    Scope='REGIONAL',
    Id='43b16080-94e8-4dbf-9b4e-166898878bc0',
)

def waf_get_web_acl():

    json_list = json.dumps(response)

    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/waf-get-web-acl.json')
    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()


