import boto3
import json
import os


def waf_list_resource_web_acl(region, AWS_ACCESS_KEY, AWS_SECRET_KEY):
    client = boto3.client('wafv2', region_name=region,
                          aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    script_dir = os.path.dirname('.')
    file_name = 'data/waf-list-web-acl-'+region+'.json'
    file_path_read = os.path.join(script_dir, file_name)
    f = open(file_path_read, 'r')
    waf_object = json.load(f)
    for waf in waf_object['WebACLs']:
        # get the web arn from the cloudtrail object
        webARN = waf['ARN']
        response = client.list_resources_for_web_acl(
            WebACLArn=webARN,
        )
        json_list = json.dumps(response)
        script_dir = os.path.dirname('.')
        file_path_write_list_resource = os.path.join(
            script_dir, 'data/waf-list-resource/waf-list-resource-web-acl-' +
            waf['Name']+'-'
            + region+'.json')
        # write the json file to the data/waf-list-resource folder
        with open(file_path_write_list_resource, 'w')as outfile:
            outfile.write(json_list)
            outfile.close()

        #     # write resource tags for every resource inside the webACL
        #     response3 = client.list_tags_for_resource(
        #         ResourceARN=webARN
        #     )
        #     json_list_3 = json.dumps(response3)
        #     script_dir = os.path.dirname('.')
        #     file_path_write_list_waf_tags = os.path.join(
        #         script_dir, 'data/waf-list-tags/waf-list-tags-' +
        #         response2['WebACL']
        #         ['Name']+'-'+region+'.json')
        #     with open(file_path_write_list_waf_tags, 'w')as outfile:
        #         outfile.write(json_list_3)
        #         outfile.close()
