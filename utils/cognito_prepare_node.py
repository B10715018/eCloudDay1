import os
import json


def cognito_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read_cognito = os.path.join(
        script_dir, 'data/cognito-list-identity-pools-'+region+'.json')
    with open(file_path_read_cognito, 'r') as openfile_cognito:
        cognito_object = json.load(openfile_cognito)
        openfile_cognito.close()
    for cognito in cognito_object['IdentityPools']:
        print(cognito)


cognito_prepare_node('us-west-2', '758325631830', [])
