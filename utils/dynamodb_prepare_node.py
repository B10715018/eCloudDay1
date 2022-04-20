import os
import json

''' Prepare all the dynamodb tables'''


def dynamodb_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/dynamodb-list-table-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        ddb_object = json.load(openfile)
        for item in ddb_object['TableNames']:
            file_path_read_ddb = os.path.join(
                script_dir, 'data/dynamodb-table/dynamoDB-item-list-scan-'+region+'-'+item+'.json')
            with open(file_path_read_ddb, 'r')as openfile_ddb:
                ddb_items = json.load(openfile_ddb)
                cytoscape_node_data.append({
                    "data": {
                        "type": "dynamodb",
                        "id": 'ddb:'+item,
                        "region": region,
                        "name": item,
                        "account_id": account_id,
                        "itemCount": ddb_items["Count"],
                        "items": ddb_items["Items"]
                    }
                })
        openfile.close()
