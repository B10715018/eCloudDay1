from http import client
import boto3
import json
import os

client = boto3.client('wafv2', region_name='us-west-2')

def waf_list_resource_web_acl():

    response = client.list_resources_for_web_acl(
        WebACLArn='arn:aws:wafv2:us-west-2:758325631830:regional/webacl/wafELB/43b16080-94e8-4dbf-9b4e-166898878bc0',
    )

    json_list = json.dumps(response)
    json_list = json.dumps(response)

    for items in response["ResourceArns"]:
        arnInfo = items.split(":")
        string = []
        for value in arnInfo:
            string.append(value)
        resourceType = string[-1].split("/")[0]


    # response2 = client.get_web_acl_for_resource(
    #     ResourceArn='arn:aws:elasticloadbalancing:us-west-2:758325631830:loadbalancer/app/appELB/5982e05975655deb'
    # )
    # print(response2)

    script_dir = os.path.dirname('.')
    file_path = os.path.join(
        script_dir, 'data/swaf-list-resource-web-acl.json')
    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()