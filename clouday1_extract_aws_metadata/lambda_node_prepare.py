import os
import json

''' Prepare all the lambda'''


def lambda_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/lambda-list-functions-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        lambda_object = json.load(openfile)
        openfile.close()
        for item in lambda_object['Functions']:
            file_path_read_tag=os.path.join(script_dir,
            'data/lambda-list-tags/lambda-list-tags-'+item["FunctionName"]+'.json')
            with open(file_path_read_tag,'r') as openfile_tag:
                lambda_tag_object=json.load(openfile_tag)
                openfile_tag.close()
            lambda_tag=lambda_tag_object['Tags']
            lambda_runtime=''
            if('Runtime' in item):
                lambda_runtime=item['Runtime']
            vpcId=''
            subnetId=[]
            if('VpcConfig' in item):
                vpcId='arn:aws:ec2:'+region+':'+account_id+':vpc/'+item['VpcConfig']['VpcId']
                for subnet in item['VpcConfig']['SubnetIds']:
                    subnetArn='arn:aws:ec2:'+region+':'+account_id+':subnet/'+subnet
                    subnetId.append(subnetArn)
    
            cytoscape_node_data.append({
                "data": {
                    "type": "Lambda",
                    "id": item["FunctionArn"],
                    "arn": item["FunctionArn"],
                    "runtime": lambda_runtime,
                    "timeout": item["Timeout"],
                    "memory_size": item["MemorySize"],
                    "version": item["Version"],
                    "region": region,
                    "account_id": account_id,
                    "name": item['FunctionName'],
                    "description": item['Description'],
                    "role": item['Role'],
                    "codesize": item['CodeSize'],
                    "vpc": vpcId,
                    "subnet": subnetId,
                    "tag": lambda_tag,
                    "console_url" : "https://"+region+".console.aws.amazon.com/lambda/home?region="+region+"#/functions/"+item['FunctionName'],
                    "cost_for_month": 0.03
                }
            })
