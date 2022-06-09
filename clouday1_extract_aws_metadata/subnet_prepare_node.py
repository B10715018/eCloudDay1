import os
import json

def subnet_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read_subnet = os.path.join(
        script_dir, 'data/ec2-describe-subnet-'+region+'.json')
    with open(file_path_read_subnet, 'r') as openfile_subnet:
        subnet_object = json.load(openfile_subnet)
        openfile_subnet.close()
    for subnet in subnet_object["Subnets"]:
        # name
        subnetKeyName=""
        if("Tags" in subnet.keys()):
            for tags in subnet['Tags']:
                if(tags['Key']=='Name'):
                    subnetKeyName = tags['Value']
        subnetId = subnet['SubnetId']
        # cidr block
        cidrBlock=subnet['CidrBlock']
        # tags
        subnet_tag={}
        if("Tags" in subnet.keys()):
            for tags in subnet['Tags']:
                subnet_tag[tags['Key']]=tags['Value']
        # state
        state=''
        state=subnet['State']
        # availability zone
        availability_zone=''
        availability_zone=subnet['AvailabilityZone']
        # availabilityZoneId
        availabilityZoneId=''
        availabilityZoneId=subnet['AvailabilityZoneId']
        #available ip address count
        availableIpAddressCount=''
        availableIpAddressCount=subnet['AvailableIpAddressCount']
        #default for az
        defaultForAz=''
        defaultForAz=subnet['DefaultForAz']
        #map public ip on launch
        mapPublicIpOnLaunch=''
        mapPublicIpOnLaunch=subnet['MapPublicIpOnLaunch']
        # map customer owned ip on launch
        mapCustomerOwnedIpOnLaunch=''
        mapCustomerOwnedIpOnLaunch=subnet['MapCustomerOwnedIpOnLaunch']
        #vpc
        vpcId=''
        vpcId=subnet['VpcId']
        #subnetArn
        subnetArn=''
        subnetArn=subnet['SubnetArn']
        #ipv6Cidr
        ipv6Cidr=[]
        ipv6Cidr=subnet['Ipv6CidrBlockAssociationSet']
        #privateDnsNameOptionOnLaunch
        privateDnsNameOptionsOnLaunch={}
        privateDnsNameOptionsOnLaunch=subnet['PrivateDnsNameOptionsOnLaunch']
        cytoscape_node_data.append({
            "data": {
                "id": subnetArn,
                "arn": subnetArn,
                "type": "Subnet",
                "name": subnetKeyName,
                "account_id": account_id,
                "region": region,
                "state": state,
                "cidr_block": cidrBlock,
                "availability_zone": availability_zone,
                "availability_zone_id": availabilityZoneId,
                "available_ip_address_count": availableIpAddressCount,
                "default_for_az":defaultForAz,
                "map_public_ip_on_launch": mapPublicIpOnLaunch,
                "map_customer_owned_ip_on_launch": mapCustomerOwnedIpOnLaunch,
                "vpc":'arn:aws:ec2:'+region+':'+account_id+':vpc/'+vpcId,
                "ipv6_cidr_block_association_set": ipv6Cidr,
                "private_dns_name_options_on_launch": privateDnsNameOptionsOnLaunch,
                "tag": subnet_tag,
                "console_url" : "https://"+region+".console.aws.amazon.com/ec2/v2/home?region="+region+"#InstanceDetails:instanceId="+subnetId,
                "cost_for_month": 6.30
            }
        })
