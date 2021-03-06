import os
import json


def edge_apigw_to_lambda_find(cytoscape_edge_data, cytoscape_node_data):
    list_of_files = os.listdir('./data/lambda-get-policy')
    # each file read description policy of one lambda
    for each_file in list_of_files:
        # since its all type str you can simply use startswith
        if each_file.startswith('lambda-arn'):
            script_dir = os.path.dirname('./data/lambda-get-policy/')
            file_path_read_connection = os.path.join(script_dir, each_file)
            with open(file_path_read_connection, 'r') as openfile:
                sns_lambda_description = json.load(openfile)
                modified_policy = json.loads(sns_lambda_description['Policy'])
                # in this policy there would be stated one or several service that could trigger lambda
                for items in (modified_policy['Statement']):
                    try:
                        lambdaArn = items['Resource']
                        triggerArn = items['Condition']['ArnLike']['AWS:SourceArn']
                        # check if source trigger is apigw
                        if('apigateway.amazonaws.com' in items['Principal']['Service']):
                            # split the arn into suitable arn only for api gateway
                            triggerArn = (json.dumps(triggerArn)
                                        ).split('/')[0][1:]
                            print('Found connection between API Gateway{} and lambda{}'.
                                format(triggerArn, lambdaArn))
                            # put data into cytoscape_edge_data
                            # check whether api exist or not in cytoscape node data
                            for node in cytoscape_node_data:
                                if triggerArn in node['data']['id']:
                                    data_api_lambda = {
                                        "data": {
                                            "id": "edge_"+triggerArn+'_to_'+lambdaArn,
                                            "source": triggerArn,
                                            "target": lambdaArn
                                        }
                                    }
                                    if(cytoscape_edge_data.count(data_api_lambda) == 0):
                                        cytoscape_edge_data.append(data_api_lambda)
                    except:
                        print('Something error happen when creating apigw and lambda edge')