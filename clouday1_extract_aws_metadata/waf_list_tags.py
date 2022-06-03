import boto3
import json
import os


def waf_list_tags(region, AWS_ACCESS_KEY, AWS_SECRET_KEY):
    client = boto3.client('wafv2', region_name=region,
                          aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    script_dir = os.path.dirname('.')
    file_name_waf='data/waf-list-web-acl-'+region+'.json'
    file_path_read_waf=os.path.join(script_dir,file_name_waf)
    with open(file_path_read_waf,'r') as openfile:
        waf_object=json.load(openfile)
        openfile.close()

    for waf in waf_object['WebACLs']:
        # write resource tags for every resource inside the webACL
        response = client.list_tags_for_resource(
            ResourceARN=waf['ARN']
        )
        json_list = json.dumps(response)
        
        file_path_write_list_waf_tags = os.path.join(
            script_dir, 'data/waf-list-tags/waf-list-tags-' +
            waf['Name']+'-'+region+'.json')
        with open(file_path_write_list_waf_tags, 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
