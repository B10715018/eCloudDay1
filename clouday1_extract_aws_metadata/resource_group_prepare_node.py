import os
import json

'''Prepare all the resource group'''


def resource_group_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/resource-group-list-groups-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        rg_object = json.load(openfile)
        openfile.close()
        for item in rg_object['Groups']:
            file_path_read_tag=os.path.join(script_dir,
            'data/rg-list-tags/get-bucket-tagging-'+item['Name']+'-'+region+'.json')
            rg_tag_object={}
            try:
                with open(file_path_read_tag,'r') as openfile_tag:
                    rg_tag_object=json.load(openfile_tag)
                    openfile_tag.close()
            except:
                print('file not exist')
            filtered_rg_tag={}
            if('TagSet' in rg_tag_object):
                for tag in rg_tag_object['TagSet']:
                    filtered_rg_tag[tag['Key']]=tag['Value']
            cytoscape_node_data.append({
                "data": {
                    "type": "rg",
                    "id": "arn:aws:rg:::"+item["Name"],
                    "arn": "arn:aws:rg:::"+item["Name"],
                    "region": region,
                    "account_id": account_id,
                    "name": item['Name'],
                    "CreationDate":item['CreationDate'],
                    "tag":filtered_rg_tag,
                    "cost_for_month": 0.26
                }
            })
