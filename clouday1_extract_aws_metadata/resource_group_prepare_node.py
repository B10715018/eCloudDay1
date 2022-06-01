import os
import json


def resource_group_prepare_node(region, account_id, cytoscape_node_data):
    '''Prepare for resource group'''
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/resource-group-list-groups--'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        resource_group_object = json.load(openfile)
        openfile.close()
        count=0
        groupARN=[]
        groupName=[]
        for item in resource_group_object['GroupIdentifiers']:
            groupARN.append(item['GroupArn'])
            groupName.append(item['GroupName'])
            count+=1
        for i in range(count):
            cytoscape_node_data.append({
                "data": {
                    "type": "Resource-Group",
                    "id": groupARN,
                    "arn": groupARN,
                    "account_id": account_id,
                    "region": region,
                    "name": groupName,
                    "cost_for_month": 0.00
                    }
                })
