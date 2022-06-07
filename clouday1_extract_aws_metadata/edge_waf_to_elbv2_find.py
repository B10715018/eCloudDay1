import os
import json

'''FIND CONNECTION BETWEEN WAF AND ELB'''

# this edge can connect waf to any kind of AWS service
def edge_waf_to_elbv2_find(cytoscape_edge_data,cytoscape_node_data,region):
    script_dir=os.path.dirname('.')
    file_name='data/waf-list-web-acl-'+region+'.json'
    file_path_read_waf=os.path.join(script_dir,file_name)
    with open(file_path_read_waf,'r') as openfile_waf:
        waf_object=json.load(openfile_waf)
        openfile_waf.close()
    for waf in waf_object['WebACLs']:
        # get all the resource related to WAF
        # use try clause here
        try:
            file_name='data/waf-list-resource/waf-list-resource-web-acl-'+waf['Name']+\
                '-'+region+'.json'
            file_path_read_resources=os.path.join(script_dir,file_name)
            with open(file_path_read_resources,'r') as openfile_resource:
                resource_object=json.load(openfile_resource)
                openfile_resource.close()

            for resourceArn in resource_object['ResourceArns']:
                for data in cytoscape_node_data:
                    nodeArn=data['data']['id']
                    if(nodeArn==resourceArn):
                        print('resourceArn:{} exist in the noden and have connection with WAF: {}'.format(resourceArn, waf['ARN']))
                        data_waf_to_resource={
                            "data": {
                                "id": "edge_"+waf['ARN']+"_"+resourceArn,
                                "source":waf['ARN'],
                                "target":resourceArn,
                            }
                        }
                        if(cytoscape_edge_data.count(data_waf_to_resource) == 0):
                            cytoscape_edge_data.append(data_waf_to_resource)
                        break
        except:
            print('No resource in waf is found')
