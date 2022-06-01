import os
import json

'''FIND CONNECTION BETWEEN ELB AND EC2'''

def edge_elbv2_to_ec2_find(region, account_id, cytoscape_edge_data):
    
    # read laod balancer object
    script_dir=os.path.dirname('.')
    file_path_read_load_balancer=os.path.join(
        script_dir,'data/elbv2-describe-load-balancer-'+region+'.json')
    with open(file_path_read_load_balancer,'r') as openfile_load_balancer:
        load_balancer_object=json.load(openfile_load_balancer)
        openfile_load_balancer.close()
    for elb in load_balancer_object['LoadBalancers']:
        elbName = elb['LoadBalancerName']
        elbArn = elb['LoadBalancerArn']

        # read elb target group  
        file_path_read_target_group = os.path.join(
            script_dir, 'data/elbv2-target-group/elbv2-describe-target-group-'+elbName+'.json')
        with open(file_path_read_target_group, 'r') as openfile_target_group:
            target_group_object = json.load(openfile_target_group)
            openfile_target_group.close()
        for targetgroup in target_group_object['TargetGroups']:
            targetgroupName = targetgroup['TargetGroupName']
            targetgroupType= targetgroup['TargetType']

            # read elb target group health  
            file_path_read_target_health = os.path.join(
            script_dir, 'data/elbv2-target-health/elbv2-describe-target-health-'+targetgroupName+'.json')
            with open(file_path_read_target_health, 'r') as openfile_target_health:
                elb_target_health = json.load(openfile_target_health)
                openfile_target_health.close()
            for elbtarget in elb_target_health['TargetHealthDescriptions']:
                targetId = elbtarget['Target']['Id']
                try:
                    if(elbArn and targetgroupType == "instance"):
                        elb_ec2_edge_data = {
                                "data": {
                                    "id": "edge_"+'arn:aws:ec2:'+region+':'+account_id+':instance/'+targetId+"_"+elbArn,
                                    "source": elbArn,
                                    "target": 'arn:aws:ec2:'+region+':'+account_id+':instance/'+targetId,
                                }
                            }
                        if(cytoscape_edge_data.count(elb_ec2_edge_data) == 0):
                            cytoscape_edge_data.append(elb_ec2_edge_data)
                            print('Found connection between elb:{} and ec2:{}'.format(elbArn,'arn:aws:ec2:'+region+':'+account_id+':instance/'+targetId))
                except:
                        print('No connection between elb and ec2')

