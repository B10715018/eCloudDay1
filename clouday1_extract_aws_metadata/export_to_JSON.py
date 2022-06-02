import os
import json
class SetEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, set):
        return list(obj)
      return json.JSONEncoder.default(self, obj)

def export_to_JSON(cytoscape_node_data, cytoscape_edge_data):
    filtered_cytoscape_data = []
    cytoscape_miscellaneous_data = [{
        "tag": {
            "Application": [],
            "Department": [],
            "Environment": [],
            "Project": [],
            "Owner": [],
            "Others": []
        },
        "region": [],
        "resourceGroup":[],
        "type": []
    }]
    # filtered the node data into one new array consisting tag and region
    for i in range(len(cytoscape_node_data)):
        misc_tag = cytoscape_miscellaneous_data[0]['tag']
        for tag in cytoscape_node_data[i]['data']['tag']:
            node_tag = cytoscape_node_data[i]['data']['tag']
            if(tag == 'Application'):
                misc_tag['Application'].append(node_tag['Application'])
            elif(tag == 'Department'):
                misc_tag['Department'].append(node_tag['Department'])
            elif(tag == 'Owner'):
                misc_tag['Owner'].append(node_tag['Owner'])
            elif(tag == 'Environment'):
                misc_tag['Environment'].append(node_tag['Environment'])
            elif(tag == 'Project'):
                misc_tag['Project'].append(node_tag['Project'])
            else:
                misc_tag['Others'].append(node_tag[tag])
    # filter all the list into set
    for tag_key in cytoscape_miscellaneous_data[0]['tag']:
        cytoscape_miscellaneous_data[0]['tag'][tag_key] = set(
            cytoscape_miscellaneous_data[0]['tag'][tag_key])
    # filter all the region
    for i in range(len(cytoscape_node_data)):
        region_name = ''.join(cytoscape_node_data[i]['data']['region'])
        cytoscape_miscellaneous_data[0]['region'].append(region_name)
    # make region from list into set
    cytoscape_miscellaneous_data[0]['region'] = set(
        cytoscape_miscellaneous_data[0]['region'])

    # filter all the resourceGroup in node data
    for data in cytoscape_node_data:
        misc_rg = cytoscape_miscellaneous_data[0]['resourceGroup']
        if('resourceGroup' in data['data']):
            for rgArn in data['data']['resourceGroup']:
                misc_rg.append(rgArn)
    # make resourceGroup from list to set
    cytoscape_miscellaneous_data[0]['resourceGroup'] = set(
        cytoscape_miscellaneous_data[0]['resourceGroup'])

    # filter all type in the node data
    for data in cytoscape_node_data:
        misc_rg=cytoscape_miscellaneous_data[0]['type']
        misc_rg.append(data['data']['type'])
    # make type from list to set
    cytoscape_miscellaneous_data[0]['type']=set(
        cytoscape_miscellaneous_data[0]['type'])
    filtered_cytoscape_data.append(cytoscape_miscellaneous_data)
    filtered_cytoscape_data.append(cytoscape_node_data)
    filtered_cytoscape_data.append(cytoscape_edge_data)

    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/data.json')
    with open(file_path_write, 'w') as outfile:
        outfile.write(json.dumps(filtered_cytoscape_data, cls=SetEncoder))
        outfile.close()
