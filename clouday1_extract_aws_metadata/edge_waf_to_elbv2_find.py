import os
import json

'''FIND CONNECTION BETWEEN WAF AND ELB'''

def edge_waf_to_elbv2_find(cytoscape_edge_data):
 # list of files in the data directory
    list_of_files = os.listdir('./data/waf-list-resource')
    for each_file in list_of_files:
        # since its all type str you can simply use startswith
        if each_file.startswith('get-web-acl-for-resource-'):
            script_dir = os.path.dirname('./data/waf-list-resource/')
            file_path_read_web_acl = os.path.join(script_dir, each_file)
            with open(file_path_read_web_acl,'r') as openfile_web_acl:
                web_acl_object=json.load(openfile_web_acl)
                openfile_web_acl.close()
            
        # if waf resource exit
        if each_file.startswith('waf-list-resource-web-acl-'+web_acl_object['WebACL']['Name']):
            script_dir = os.path.dirname('./data/waf-list-resource/')
            file_path_read_web_acl_resource = os.path.join(script_dir, each_file)
            with open(file_path_read_web_acl_resource,'r') as openfile_web_acl_resource:
                web_acl_resource=json.load(openfile_web_acl_resource)
                openfile_web_acl_resource.close()
                for resourceArn in web_acl_resource['ResourceArns']:
                    print('Found connection between WAF {} and ELB {}'.format(web_acl_object['WebACL']['ARN'],
                    resourceArn))
                    data_waf_to_elbv2={
                        "data":{
                            "id":"edge_"+web_acl_object['WebACL']['ARN']+'_'+resourceArn,
                            "source":web_acl_object['WebACL']['ARN'],
                            "target":resourceArn
                        }
                    }
                    cytoscape_edge_data.append(data_waf_to_elbv2)

        else:
            print('No waf resource is found')
