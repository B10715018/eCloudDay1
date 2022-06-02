import boto3
import json
import os


def wafv2_list_web_acl(region, AWS_ACCESS_KEY, AWS_SECRET_KEY):
    client = boto3.client('wafv2', region_name=region,
                          aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    response = client.list_web_acls(
        Scope='REGIONAL'
    )
    json_response = json.dumps(response)
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/waf-list-web-acl-'+region+'.json')
    with open(file_path_write, 'w') as outfile:
        outfile.write(json_response)
        outfile.close()


wafv2_list_web_acl('us-west-2', 'AKIA3BD523NLHVGEZDDC',
                   '23Coye0Q6+1xRnyU4ZK4ZaY+brKx3Cag/ajAlzUV')
