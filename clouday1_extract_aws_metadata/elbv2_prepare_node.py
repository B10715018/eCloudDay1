import json
import os

'''Prepare for elb node'''


def elbv2_prepare_node(region, account_id, cytoscape_node_data):
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(
        script_dir, 'data/elbv2-describe-load-balancer-'+region+'.json')
    with open(file_path_read, 'r') as openfile:
        elb_object = json.load(openfile)
        openfile.close()

        for item in elb_object['LoadBalancers']:
            az_list = [x['ZoneName'] for x in item['AvailabilityZones']]
            each_file = 'elbv2-list-tags-' + \
                item['LoadBalancerName']+'-'+region+'.json'
            file_path_read_2 = os.path.join(
                script_dir, 'data/elbv2-list-tags/'+each_file)
            f = open(file_path_read_2, 'r')
            elb_tag_object = json.load(f)
            elb_tag = {}
            for tag in elb_tag_object[0]['Tags']:
                elb_tag[tag['Key']] = tag['Value']

            cytoscape_node_data.append({
                "data": {
                    "type": "ElbV2",
                    "id": item['LoadBalancerArn'],
                    "arn": item['LoadBalancerArn'],
                    "name": item['LoadBalancerName'],
                    "dns": item['DNSName'],
                    "account_id": account_id,
                    "region": region,
                    "vpc_id": item['VpcId'],
                    "created_time": item['CreatedTime'],
                    "lodabalancer_type": item['Type'],
                    "availability_zones": az_list,
                    "tag": elb_tag,
                    "console_url" : "https://"+"region+.console.aws.amazon.com/ec2/v2/home?region="+region+"#LoadBalancers:sort="+item['LoadBalancerName'],
                    "cost_for_month": 4.91
                }
            })
