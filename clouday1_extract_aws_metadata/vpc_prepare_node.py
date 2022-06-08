import os
import json

def vpc_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read_vpc = os.path.join(
        script_dir, 'data/ec2-describe-vpcs-'+region+'.json')
    with open(file_path_read_vpc, 'r') as openfile_vpc:
        vpc_object = json.load(openfile_vpc)
        openfile_vpc.close()
    for vpc in vpc_object["Vpcs"]:
        # name
        vpcKeyName=""
        for tags in vpc['Tags']:
            if(tags['Key']=='Name'):
                vpcKeyName = tags['Value']
        vpcId = vpc['VpcId']
        # cidr block
        cidrBlock=vpc['CidrBlock']
        # tags
        vpc_tags={}
        for tags in vpc['Tags']:
            vpc_tags[tags['Key']]=tags['Value']
        # state
        state=''
        state=vpc['State']
        # InstanceTenancy
        instanceTenancy=''
        instanceTenancy=vpc['InstanceTenancy']
        # CidrBlockAssociationSet
        cidrBlockAssociationSet=[]
        cidrBlockAssociationSet=vpc['CidrBlockAssociationSet']
        # isDefault
        isDefault=''
        isDefault=vpc['IsDefault']
        # DhcpOptionsId
        dhcpOptionsId=''
        dhcpOptionsId=vpc['DhcpOptionsId']
        cytoscape_node_data.append({
            "data": {
                "id": 'arn:aws:ec2:'+region+':'+account_id+':vpc/'+vpcId,
                "arn": 'arn:aws:ec2:'+region+':'+account_id+':vpc/'+vpcId,
                "type": "VPC",
                "name": vpcKeyName,
                "account_id": account_id,
                "region": region,
                "state": state,
                "cidr_block": cidrBlock,
                "instance_tenancy": instanceTenancy,
                "cidr_block_association_set": cidrBlockAssociationSet,
                "is_default": isDefault,
                "dhcp_options_id": dhcpOptionsId,
                "tag": vpc_tags,
                "console_url" : "https://"+region+".console.aws.amazon.com/ec2/v2/home?region="+region+"#InstanceDetails:instanceId="+vpcId,
                "cost_for_month": 6.30
            }
        })
