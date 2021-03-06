import os
import json

def ec2_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read_ec2 = os.path.join(
        script_dir, 'data/ec2-describe-instances-'+region+'.json')
    with open(file_path_read_ec2, 'r') as openfile_ec2:
        ec2_object = json.load(openfile_ec2)
        openfile_ec2.close()
    for instance in ec2_object["Reservations"]:
        # check whether or not EC2 have keyName
        for ec2 in instance['Instances']:
            ec2KeyName=""
            if('KeyName' in ec2):
                ec2KeyName = ec2['KeyName']
            ec2Id = ec2['InstanceId']
            LaunchTime= ec2['LaunchTime']
            InstanceType=ec2['InstanceType']
            #get tags for each ec2 
            ec2_tag={}
            if "Tags" in ec2:
                for tag in ec2['Tags']:
                    ec2_tag[tag['Key']]=tag['Value']
            status=''
            status=ec2['State']['Name']
            #vpc
            vpcId=''
            vpcId=ec2['VpcId']
            #subnet
            subnetId=[]
            subnetArn=''
            subnetArn=str('arn:aws:ec2:'+region+':'+account_id+':subnet/'+ec2['SubnetId'])
            subnetId.append(subnetArn)
            cytoscape_node_data.append({
                "data": {
                    "id": 'arn:aws:ec2:'+region+':'+account_id+':instance/'+ec2Id,
                    "arn": 'arn:aws:ec2:'+region+':'+account_id+':instance/'+ec2Id,
                    "type": "EC2",
                    "name": ec2KeyName,
                    "account_id": account_id,
                    "region": region,
                    "LaunchTime": LaunchTime,
                    "InstanceType": InstanceType,
                    "tag": ec2_tag,
                    "status": status,
                    "vpc":'arn:aws:ec2:'+region+':'+account_id+':vpc/'+vpcId,
                    "subnet":subnetId,
                    "console_url" : "https://"+region+".console.aws.amazon.com/ec2/v2/home?region="+region+"#InstanceDetails:instanceId="+ec2Id,
                    "cost_for_month": 6.30
                }
            })
