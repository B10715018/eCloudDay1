import os
import json

# "arn:aws:execute-api:us-west-2:758325631830:9z24ydgzs2/*/GET/\" ==> example of apigw arn


def ec2_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read_ec2 = os.path.join(
        script_dir, 'data/data/ec2-describe-instances-'+region+'.json')
    with open(file_path_read_ec2, 'r') as openfile_ec2:
        ec2_object = json.load(openfile_ec2)
        openfile_ec2.close()
    for ec2 in ec2_object["Reservations"][0]["Instances"]:
        ec2KeyName = ec2['KeyName']
        ec2Id = ec2['InstanceId']
        LaunchTime= ec2['LaunchTime']
        InstanceType=ec2['InstanceType']
        #get tags for each apigw 
        if "Tags" in ec2.keys():
            ec2Tag = ec2['Tags'] 

        
        cytoscape_node_data.append({
            "data": {
                "id": ec2Id,
                "arn": "arn:aws:execute-api:"+region+":"+account_id+":"+ec2Id,
                "type": "Ec2",
                "name": ec2KeyName,
                "account_id": account_id,
                "region": region,
                "LaunchTime": LaunchTime,
                "InstanceType": InstanceType,
                "tag": ec2Tag,
                "cost_for_month": "64.54 USD"
            }
        })
