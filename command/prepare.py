from utils.edge_lambda_ddb_find import edge_lambda_ddb_find
from utils.sfn_find_connection import sfn_find_connection
from utils.edge_lambda_sns_find import edge_lambda_sns_find
from utils.export_to_JSON import export_to_JSON
from utils.lambda_node_prepare import lambda_prepare_node
from utils.s3_prepare_node import s3_prepare_node
from utils.dynamodb_prepare_node import dynamodb_prepare_node
from utils.transcribe_prepare_node import transcribe_prepare_node
from utils.translate_prepare_node import translate_prepare_node
from utils.sns_prepare_node import sns_prepare_node
from utils.sfn_prepare_node import sfn_prepare_node
from utils.edge_lambda_to_transcribe import edge_lambda_to_transcribe
from utils.edge_lambda_to_translate import edge_lambda_to_translate_find

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

    def prepare_transcribe_node(self):
        transcribe_prepare_node(
            self.region_name, self.account_id, self.cytoscape_node_data)

    def prepare_translate_node(self):
        translate_prepare_node(
            self.region_name, self.account_id, self.cytoscape_node_data)

    def prepare_sns_node(self):
        sns_prepare_node(self.region_name, self.account_id,
                         self.cytoscape_node_data)

    def prepare_sfn_node(self):
        sfn_prepare_node(self.region_name, self.account_id,
                         self.cytoscape_node_data)

    def find_sfn_connection(self):
        sfn_find_connection(self.cytoscape_node_data, self.cytoscape_edge_data)

    def find_edge_lambda_to_sns(self):
        edge_lambda_sns_find(self.cytoscape_edge_data, self.region_name)

    def find_edge_lambda_to_ddb(self):
        edge_lambda_ddb_find(self.cytoscape_edge_data, self.region_name)

    def find_edge_lambda_to_transcribe(self):
        edge_lambda_to_transcribe(
            self.cytoscape_edge_data, self.region_name, self.account_id)

    def find_edge_lambda_to_translate(self):
        edge_lambda_to_translate_find(
            self.cytoscape_edge_data, self.region_name, self.account_id)


# initialize a class
prepare_command = Prepare(REGION_NAME, ACCOUNT_ID)

# call Prepare function ( doing the logic )

# prepare node logic
prepare_command.prepare_lambda_node()
prepare_command.prepare_s3_node()
prepare_command.prepare_dynamodb_node()
prepare_command.prepare_transcribe_node()
prepare_command.prepare_translate_node()
prepare_command.prepare_sns_node()
prepare_command.prepare_sfn_node()
# prepare edge logic
prepare_command.find_sfn_connection()
prepare_command.find_edge_lambda_to_sns()
prepare_command.find_edge_lambda_to_ddb()
prepare_command.find_edge_lambda_to_transcribe()
prepare_command.find_edge_lambda_to_translate()
# EXPORT INTO JSON FILE
prepare_command.exportToJSON()

# '''STARTING FROM HERE IS LOGIC TO FIND RELATIONSHIPS'''

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


'''FIND CONNECTION FROM LAMBDA TO STEP FUNCTION'''
'''FIND CONNECTION APIGW TO STEP FUNCTION'''
'''FIND CONNECTION S3 TO COGNITO'''
'''PREPARE FOR APIGW'''
'''FIND CONNECTION FROM SNS TO LAMBDA'''
