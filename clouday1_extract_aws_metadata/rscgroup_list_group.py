import boto3
import os
import json

def rscgroup_list_group(region):
    client = boto3.client('resource-groups', region_name=region)

    response = client.list_groups()
    json_response = json.dumps(response, indent=4)
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/rscgroup-list-group-'+region+'.json')
    with open(file_path_write, 'w') as outfile:
        outfile.write(json_response)
        outfile.close()


