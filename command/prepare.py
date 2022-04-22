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
from utils.edge_transcribe_to_s3_find import edge_transcribe_to_s3_find
from utils.apigw_prepare_node import api_gw_prepare_node
from utils.cognito_prepare_node import cognito_prepare_node
from utils.edge_s3_to_cognito_find import edge_s3_to_cognito_find
from utils.edge_lambda_to_sfn_find import edge_lambda_to_sfn_find
from utils.edge_apigw_to_lambda_find import edge_apigw_to_lambda_find
from utils.edge_sns_to_lambda_find import edge_sns_to_lambda_find

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

    def prepare_apigw_node(self):
        api_gw_prepare_node(self.region_name, self.account_id,
                            self.cytoscape_node_data)

    def prepare_cognito_node(self):
        cognito_prepare_node(
            self.region_name, self.account_id, self.cytoscape_node_data)

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

    def find_edge_transcribe_to_s3(self):
        edge_transcribe_to_s3_find(
            self.cytoscape_edge_data, self.region_name, self.account_id)

    def find_edge_s3_to_cognito(self):
        edge_s3_to_cognito_find(
            self.cytoscape_edge_data)

    def find_edge_lambda_to_sfn(self):
        edge_lambda_to_sfn_find(self.region_name,
                                self.cytoscape_edge_data)

    def find_edge_apigw_to_lambda(self):
        edge_apigw_to_lambda_find(
            self.cytoscape_edge_data, self.cytoscape_node_data)

    def find_edge_sns_to_lambda(self):
        edge_sns_to_lambda_find(self.cytoscape_edge_data)


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
prepare_command.prepare_apigw_node()
prepare_command.prepare_cognito_node()
# prepare edge logic
prepare_command.find_sfn_connection()
prepare_command.find_edge_lambda_to_sns()
prepare_command.find_edge_lambda_to_ddb()
prepare_command.find_edge_lambda_to_transcribe()
prepare_command.find_edge_lambda_to_translate()
prepare_command.find_edge_transcribe_to_s3()
prepare_command.find_edge_s3_to_cognito()
prepare_command.find_edge_lambda_to_sfn()
prepare_command.find_edge_apigw_to_lambda()
prepare_command.find_edge_sns_to_lambda()
# EXPORT INTO JSON FILE
prepare_command.exportToJSON()

'''FIND CONNECTION FROM SNS TO LAMBDA'''
