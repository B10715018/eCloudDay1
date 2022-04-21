import os
import json

def edge_sns_to_lambda_find(region,account_id,cytoscape_edge_data):
    list_of_files = os.listdir('./data/lambda-get-policy')
    for each_file in list_of_files:
        # since its all type str you can simply use startswith
        if each_file.startswith('lambda-arn'):
            script_dir=os.path.dirname('./data/lambda-get-policy/')
            file_path_read_connection=os.path.join(script_dir,each_file)
            with open(file_path_read_connection,'r') as openfile:
                 sns_lambda_description=json.load(openfile)
                 print(sns_lambda_description['Policy'])
                 with open('./data/test.json','r') as outfile:
                     outfile.write(json.dumps(sns_lambda_description['Policy']))
                     outfile.close()

edge_sns_to_lambda_find('us-west-2','758325631830',[])