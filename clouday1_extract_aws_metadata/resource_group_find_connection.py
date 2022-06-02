import os
import json


def rg_find_connection(cytoscape_node_data):
    list_of_rg_node = os.listdir('./data')
    for each_file in list_of_rg_node:
        try:
            if(each_file.startswith('resource-group-list-groups-')):
                script_dir_rg = os.path.dirname('./data/')
                file_path_read = os.path.join(script_dir_rg, each_file)
                f = open(file_path_read, 'r')
                rg_object = json.load(f)
                for group in rg_object['GroupIdentifiers']:
                    groupArn = group['GroupArn']
                    groupName = group['GroupName']
                    region = groupArn.split(':')[3]
                    file_name_rg_resource = 'resource-group-list-group-resources-' + \
                        region+'-'+groupName+'.json'
                    script_dir_resource = os.path.dirname(
                        './data/resource-group-resources/')
                    file_path_read_resource = os.path.join(
                        script_dir_resource, file_name_rg_resource)
                    f_resource = open(file_path_read_resource, 'r')
                    rg_resource_object = json.load(f_resource)
                    for resource in rg_resource_object['ResourceIdentifiers']:
                        # get all the resources
                        resourceArn = resource['ResourceArn']
                        for node in cytoscape_node_data:
                            nodeArn = node['data']['id']
                            # if node exist then update to its field
                            if(resourceArn == nodeArn):
                                # there is possibility one service have many resource group
                                resourceGroupList = []
                                if('resourceGroup' in node['data']):
                                    print('There is double data')
                                    resourceGroupList = node['data']['resourceGroup']
                                resourceGroupList.append(groupName)
                                print('node is in resourceGroup:', groupName)
                                node['data'].update({
                                    'resourceGroup': resourceGroupList
                                })
        except:
            print('Error in resource group find connection')
