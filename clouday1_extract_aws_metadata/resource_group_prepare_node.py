import os
import json


def resource_group_prepare_node(region, account_id, cytoscape_node_data):
    '''Prepare for resource group'''
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/resource-group-list-groups-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        resource_group_object = json.load(openfile)
        openfile.close()
        for item in resource_group_object['GroupIdentifiers']:
            file_path_read_tag = os.path.join(script_dir,
            'data/resource-group-list-tags/resource-group-list-tags-'+region+'-'+item['GroupName']+'.json')
            resource_group_tag_object = {}
            try:
                with open(file_path_read_tag, 'r') as openfile_tag:
                    resource_group_tag_object = json.load(openfile_tag)
                    openfile_tag.close()
                    resource_group_tag = resource_group_tag_object['Tags']
            except:
                print('file not exist')
            file_path_read_resource = os.path.join(script_dir,
            'data/resource-group-resources/resource-group-list-group-resources-'+region+'-'+item['GroupName']+'.json')
            with open(file_path_read_resource,'r') as openfile_resource:
                rg_resource_object=json.load(openfile_resource)
                openfile_resource.close()
                rg_resource=[]
                for resource in rg_resource_object['Resources']:
                    rg_resource.append(resource['Identifier']['ResourceArn'])
            cytoscape_node_data.append({
                "data": {
                    "type": "Resource-Group",
                    "id": item['GroupArn'],
                    "arn": item['GroupArn'],
                    "account_id": account_id,
                    "region": region,
                    "name": item['GroupName'],
                    "tag": resource_group_tag,
                    "console_url" : "https://"+region+".console.aws.amazon.com/resource-groups/group/"+item['GroupName']+"?region="+region,
                    "resource" : rg_resource,
                    "cost_for_month": 0.00
                }
            })
