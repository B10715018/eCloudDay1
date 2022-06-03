import os
import json

''' Prepare all the wab acl'''

def waf_prepare_node(region, account_id, cytoscape_node_data):
    script_dir=os.path.dirname('.')
    file_name='data/waf-list-web-acl-'+region+'.json'
    file_path_read_waf=os.path.join(script_dir,file_name)
    with open(file_path_read_waf,'r') as openfile_waf:
        waf_object=json.load(openfile_waf)
        openfile_waf.close()
    try:
        for waf in waf_object['WebACLs']:
            # all resource associated with WAF
            file_name_resource='data/waf-list-resource/waf-list-resource-web-acl-'+waf['Name']+'-'+region+'.json'
            file_path_read_resource=os.path.join(script_dir,file_name_resource)
            with open(file_path_read_resource,'r') as openfile_resource:
                waf_resource_object=json.load(openfile_resource)
                openfile_resource.close()
            resourceList=[]
            for resource in waf_resource_object['ResourceArns']:
                resourceList.append(resource)
            # tags asscocaited with WAF
            file_name_tag='data/waf-list-tags/waf-list-tags-'+waf['Name']+'-'+region+'.json'
            file_path_read_tag=os.path.join(script_dir,file_name_tag)
            with open(file_path_read_tag,'r') as openfile_tag:
                tag_object=json.load(openfile_tag)
                openfile_tag.close()
            tagList={}
            for tag in tag_object['TagInfoForResource']['TagList']:
                tagList[tag['Key']]=tag['Value']
            cytoscape_node_data.append({
                "data": {
                    "type": "WAF",
                    "id": waf['ARN'],
                    "region": region,
                    "name": waf['Name'],
                    "resources": resourceList,
                    "account_id": account_id,
                    "console_url" : "https://"+region+".console.aws.amazon.com/wafv2/homev2/web-acls?region="+region,
                    "cost_for_month": 5.22,
                    "tag": tagList
                }
            })
    except:
        print('Something Error in WAF prepare')
