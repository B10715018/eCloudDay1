import boto3
import json
import os


def resource_group_list_groups(region):
    client = boto3.client('resource-groups', region_name=region)
    response = client.list_groups()

    json_list = json.dumps(response)
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/resource-group-list-groups-'+region+'.json')
    with open(file_path_write, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()
