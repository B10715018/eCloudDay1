from utils.export_to_JSON import export_to_JSON
from utils.lambda_node_prepare import lambda_prepare_node
from utils.s3_prepare_node import s3_prepare_node
from utils.dynamodb_prepare_node import dynamodb_prepare_node

REGION_NAME = 'us-west-2'
ACCOUNT_ID = '758325631830'


class Prepare:
    def __init__(self, region_name, account_id):
        self.region_name = region_name
        self.account_id = account_id
        self.cytoscape_node_data = []
        self.cytoscape_edge_data = []

    def exportToJSON(self):
        export_to_JSON(self.cytoscape_node_data, self.cytoscape_edge_data)

    def prepare_lambda_node(self):
        lambda_prepare_node(self.region_name, self.account_id,
                            self.cytoscape_node_data)

    def prepare_s3_node(self):
        s3_prepare_node(self.region_name, self.account_id,
                        self.cytoscape_node_data)

    def prepare_dynamodb_node(self):
        dynamodb_prepare_node(
            self.region_name, self.account_id, self.cytoscape_node_data)


# initialize a class
prepare_command = Prepare(REGION_NAME, ACCOUNT_ID)

# call Prepare function
prepare_command.prepare_lambda_node()
prepare_command.prepare_s3_node()
prepare_command.prepare_dynamodb_node()
prepare_command.exportToJSON()

# ''' Prepare all the dynamodb tables'''
# with open('./data/dynamodb-list-table.json', 'r') as openfile:
#     ddb_object = json.load(openfile)
#     for item in ddb_object['TableNames']:
#         cytoscape_node_data.append({
#             "data": {
#                 "type": "dynamodb",
#                 "id": 'ddb:'+item,
#                 "region": "us-west-2",
#                 "name": item,
#             }
#         })
#     openfile.close()

# '''Prepare for transcribe'''
# list_of_files = os.listdir('./data')  # list of files in the data directory
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('cloudtrail-start-transcription'):
#         print('Found a cloudtrail transcribe file')
#         cytoscape_node_data.append({
#             "data": {
#                 "type": "transcribe",
#                 "id": "transcribe",
#                 "region": "us-west-2",
#                 "name": "transcribe",
#             }
#         })
#         break

# '''Prepare for translate'''
# list_of_files = os.listdir('./data')  # list of files in the data directory
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('cloudtrail-translate-text-'):
#         print('Found a cloudtrail translate file')
#         cytoscape_node_data.append({
#             "data": {
#                 "type": "translate",
#                 "id": "translate",
#                 "region": "us-west-2",
#                 "name": "translate",
#             }
#         })
#         break

# '''Prepare for step function'''
# with open('./data/step-function-list-state-machine.json', 'r') as openfile:
#     sfn_object = json.load(openfile)
#     for sfn in sfn_object['stateMachines']:
#         cytoscape_node_data.append({
#             "data": {
#                 "type": "step-function",
#                 "id": sfn['stateMachineArn'],
#                 "region": 'us-west-2',
#                 "name": sfn['name'],
#             }
#         })

#     openfile.close()

# '''Prepare for SNS'''
# with open('./data/sns-list-topic-us-west-2.json', 'r') as openfile:
#     sns_object = json.load(openfile)
#     for sns in sns_object['Topics']:
#         cytoscape_node_data.append({
#             "data": {
#                 "type": "sns",
#                 "id": sns['TopicArn'],
#                 "region": 'us-west-2',
#                 "name": sns['TopicArn'],
#             }
#         })
#     openfile.close()

# '''STARTING FROM HERE IS LOGIC TO FIND RELATIONSHIPS'''

# '''FIND CONNECTION INSIDE STEP FUNCTION'''
# list_of_files = os.listdir('./data')  # list of files in the data directory
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('sfn-definition-'):
#         with open('./data/' + each_file, 'r') as openfile:
#             unfiltered_sfn_arn = each_file[15:]
#             filtered_sfn_arn = unfiltered_sfn_arn.split('.')[0]
#             try:
#                 sfn_connection_object = json.load(openfile)
#                 listOfStates = list(sfn_connection_object['States'].values())
#                 totalStates = len(sfn_connection_object['States'].keys())
#                 for i in range(totalStates):
#                     # sourceId for edge
#                     sourceId = ''
#                     # if state is lambda
#                     if('lambda' in listOfStates[i]['Resource']):
#                         print('Lambda Found in SFN')
#                         sourceId = (
#                             listOfStates[i]['Parameters']['FunctionName'])[:-8]
#                         for item in cytoscape_node_data:
#                             if item['data']['id'] == sourceId:
#                                 item['data'].update(
#                                     {"parent": filtered_sfn_arn})
#                     # if state is sns
#                     if('sns' in listOfStates[i]['Resource']):
#                         # give the last state parent node
#                         print('SNS Found in SFN')
#                         sourceId = (listOfStates[i]['Parameters']['TopicArn'])
#                         for item in cytoscape_node_data:
#                             if item['data']['id'] == sourceId:
#                                 item['data'].update(
#                                     {"parent": filtered_sfn_arn})
#                     # if this is not end state
#                     if(i != totalStates-1):
#                         print('this is not end state', i)
#                         targetId = ''
#                         # if next state is lambda
#                         if('lambda' in listOfStates[i+1]['Resource']):
#                             targetId = (
#                                 listOfStates[i+1]['Parameters']['FunctionName'])[:-8]
#                         # if next state is sns
#                         if('sns' in listOfStates[i+1]['Resource']):
#                             targetId = (
#                                 listOfStates[i+1]['Parameters']['TopicArn'])
#                         # edge data
#                         sfn_edge_data = {
#                             "data": {
#                                 "id": sourceId+'-'+targetId,
#                                 "source": sourceId,
#                                 "target": targetId,
#                             }
#                         }
#                         cytoscape_edge_data.append(sfn_edge_data)

#             except:
#                 print('No connection inside step function')
#         openfile.close()

# '''FIND CONNECTION BETWEEN LAMBDA AND SNS'''
# for item in lambda_object['Functions']:
#     for sns in sns_object['Topics']:
#         try:
#             if(item['Environment']['Variables']['SNS_TOPIC'] == sns['TopicArn']):
#                 print('Found connection between lambda{} and sns{}'.format(
#                     item['FunctionName'], sns['TopicArn']))
#                 lambda_sns_edge_data = {
#                     "data": {
#                         "id": item['FunctionArn']+'-'+sns['TopicArn'],
#                         "source": item['FunctionArn'],
#                         "target": sns['TopicArn'],
#                     }
#                 }
#                 if(cytoscape_edge_data.count(lambda_sns_edge_data) == 0):
#                     cytoscape_edge_data.append(lambda_sns_edge_data)
#                 cytoscape_edge_data.append(lambda_sns_edge_data)
#         except:
#             print('No connection between lambda{} and sns{}'.format(
#                 item['FunctionName'], sns['TopicArn'])
#             )

# '''FIND CONNECTION BETWEEN DDB AND LAMBDA'''
# for item in lambda_object['Functions']:
#     for ddb in ddb_object['TableNames']:
#         try:
#             if item['Environment']['Variables']['DB_TABLE_NAME'] == ddb:
#                 # print('Found connection between {} and {}'.format(
#                 #     item['FunctionName'], ddb))
#                 cytoscape_edge_data.append({
#                     "data": {
#                         "id": item['FunctionName'] + '-ddb:' + ddb,
#                         "source": item["FunctionArn"],
#                         "target": 'ddb:'+ddb,
#                     }
#                 })
#         except:
#             print('No connection between {} and {}'.format(
#                 item['FunctionName'], ddb))

# '''FIND CONNECTION BETWEEN LAMBDA AND TRANSCRIBE'''
# list_of_files = os.listdir('./data')  # list of files in the data directory
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('cloudtrail-start-transcription'):
#         with open('./data/' + each_file, 'r') as openfile:
#             cloudtrail_transcribe_object = json.load(openfile)
#             try:
#                 if 'AWS_Lambda' in cloudtrail_transcribe_object['userAgent']:
#                     lambda_arn = 'arn:aws:lambda:'+REGION_NAME+':'+ACCOUNT_ID + \
#                         ':function:' + \
#                         (cloudtrail_transcribe_object['userIdentity']
#                          ['principalId'].split(':')[-1])
#                     transcribe_edge_data = {
#                         "data": {
#                             "id": lambda_arn+'-'+'transcribe',
#                             "source": lambda_arn,
#                             "target": 'transcribe',
#                         }
#                     }
#                     if(cytoscape_edge_data.count(transcribe_edge_data) == 0):
#                         cytoscape_edge_data.append(transcribe_edge_data)
#                     print('Found connection between transcribe and lambda:{}'.format(
#                         cloudtrail_transcribe_object['userIdentity']['principalId'].split(':')[-1]))
#             except:
#                 print('No connection between lambda and transcribe')
#         openfile.close()

# '''FIND CONNECTION BETWEEN TRANSCRIBE AND S3'''
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('cloudtrail-start-transcription'):
#         with open('./data/' + each_file, 'r') as openfile:
#             cloudtrail_transcribe_object = json.load(openfile)
#             try:
#                 for s3 in s3_object['Buckets']:
#                     if(cloudtrail_transcribe_object['requestParameters']['outputBucketName'] == s3['Name']):
#                         transcribe_s3_edge_data = {
#                             "data": {
#                                 "id": 'transcribe-'+'s3:'+s3['Name'],
#                                 "source": 'transcribe',
#                                 "target": 's3:'+s3['Name'],
#                             }
#                         }
#                         if(cytoscape_edge_data.count(transcribe_s3_edge_data) == 0):
#                             cytoscape_edge_data.append(transcribe_s3_edge_data)
#                             print('Found connection between transcribe and s3:{}'.format(
#                                 cloudtrail_transcribe_object['requestParameters']['outputBucketName']))
#             except:
#                 print('No connection between transcribe and s3 bucket:{}'.format(
#                     cloudtrail_transcribe_object['requestParameters']['outputBucketName']
#                 ))
#         openfile.close()

# '''FIND CONNECTION BETWEEN LAMBDA AND TRANSLATE'''
# list_of_files = os.listdir('./data')  # list of files in the data directory
# for each_file in list_of_files:
#     # since its all type str you can simply use startswith
#     if each_file.startswith('cloudtrail-translate-text-'):
#         with open('./data/' + each_file, 'r') as openfile:
#             cloudtrail_translate_object = json.load(openfile)
#             try:
#                 if 'AWS_Lambda' in cloudtrail_translate_object['userAgent']:
#                     lambda_arn = 'arn:aws:lambda:'+REGION_NAME+':'+ACCOUNT_ID + \
#                         ':function:' + \
#                         (cloudtrail_translate_object['userIdentity']
#                          ['principalId'].split(':')[-1])
#                     translate_edge_data = {
#                         "data": {
#                             "id": lambda_arn+'-'+'translate',
#                             "source": lambda_arn,
#                             "target": 'translate',
#                         }
#                     }
#                     if(cytoscape_edge_data.count(translate_edge_data) == 0):
#                         cytoscape_edge_data.append(translate_edge_data)
#                     print('Found connection between translate and lambda:{}'.format(
#                         cloudtrail_translate_object['userIdentity']['principalId'].split(':')[-1]))
#             except:
#                 print('No connection between lambda and translate')
#         openfile.close()

# filtered_cytoscape_data.append(cytoscape_node_data)
# filtered_cytoscape_data.append(cytoscape_edge_data)
