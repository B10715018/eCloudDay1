import os
import json

''' Prepare all the wab acl'''

def webacl_prepare_node(region, account_id, cytoscape_node_data):

    list_of_files = os.listdir('./data/waf-list-resource')
    for each_file in list_of_files:
        # since its all type str you can simply use startswith
        if each_file.startswith('get-web-acl-for-resource-'):
          # open every file in waf-list-resource folder inside data folder
            script_dir = os.path.dirname('.')
            file_path_read = os.path.join(
                script_dir, 'data/waf-list-resource/'+each_file)
            with open(file_path_read, 'r') as openfile:
                web_acl_object = json.load(openfile)
                openfile.close()
            web_acl_rules = [x['Name'] for x in web_acl_object['WebACL']['Rules']]
            cytoscape_node_data.append({
                "data": {
                    "type": "WebAcl",
                    "id": web_acl_object['WebACL']['Id'],
                    "region": region,
                    "name": web_acl_object['WebACL']['Name'],
                    "account_id": account_id,
                    "rules": web_acl_rules,
                    "console_url" : "https://"+region+".console.aws.amazon.com/wafv2/homev2/web-acls?region="+region,
                    "cost_for_month": 5.22
                }
            })