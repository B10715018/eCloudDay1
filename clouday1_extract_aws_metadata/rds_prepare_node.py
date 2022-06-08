import json
import os

'''Prepare for rds node'''


def rds_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/rds-describe-instance-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        rds_object = json.load(openfile)
        openfile.close()
        for item in rds_object['DBInstances']:
            rds_tag = {}
            for tag in item['TagList']:
                rds_tag[tag['Key']]=tag['Value']
            #vpc
            vpcId=''
            vpcId='arn:aws:ec2:'+region+':'+account_id+':vpc/'+item['DBSubnetGroup']['VpcId']
            #subnet(list)
            subnetId=[]
            for subnet in item['DBSubnetGroup']['Subnets']:
                subnetArn='arn:aws:ec2:'+region+':'+account_id+':subnet/'+subnet['SubnetIdentifier']
                subnetId.append(subnetArn)

            cytoscape_node_data.append({
            "data": {
                "type": "RDS",
                "id" : item['DBInstanceArn'],
                "arn": item['DBInstanceArn'],
                "name": item['DBInstanceIdentifier'],
                "account_id": account_id,
                "region": region,
                "engine_type": item['Engine'],
                "instance_type": item['DBInstanceClass'],
                "storage_type": item['StorageType'],
                "launch_time" :item['InstanceCreateTime'],
                "instance_status": item['DBInstanceStatus'],
                "vpc_security_group": item['VpcSecurityGroups'][0]['VpcSecurityGroupId'],
                "vpc":vpcId,
                "subnet":subnetId,
                "tag":rds_tag,
                "console_url" : "https://"+region+".console.aws.amazon.com/rds/home?region="+region+"#database:id="+item['DBInstanceIdentifier']+";is-cluster=false",
                "cost_for_month": 14.4,
                }
            })
