from clouday1_extract_aws_metadata.export_to_JSON import export_to_JSON
from clouday1_extract_aws_metadata.lambda_node_prepare import lambda_prepare_node
from clouday1_extract_aws_metadata.s3_prepare_node import s3_prepare_node
from clouday1_extract_aws_metadata.dynamodb_prepare_node import dynamodb_prepare_node
from clouday1_extract_aws_metadata.transcribe_prepare_node import transcribe_prepare_node
from clouday1_extract_aws_metadata.translate_prepare_node import translate_prepare_node
from clouday1_extract_aws_metadata.sns_prepare_node import sns_prepare_node
from clouday1_extract_aws_metadata.sfn_prepare_node import sfn_prepare_node
from clouday1_extract_aws_metadata.apigw_prepare_node import api_gw_prepare_node
from clouday1_extract_aws_metadata.cognito_prepare_node import cognito_prepare_node
from clouday1_extract_aws_metadata.sfn_find_connection import sfn_find_connection
from clouday1_extract_aws_metadata.edge_apigw_to_lambda_find import edge_apigw_to_lambda_find
from clouday1_extract_aws_metadata.edge_sns_to_lambda_find import edge_sns_to_lambda_find
from clouday1_extract_aws_metadata.edge_lambda_ddb_find import edge_lambda_ddb_find
from clouday1_extract_aws_metadata.edge_lambda_to_transcribe import edge_lambda_to_transcribe
from clouday1_extract_aws_metadata.edge_lambda_to_translate import edge_lambda_to_translate_find
from clouday1_extract_aws_metadata.edge_s3_to_cognito_find import edge_s3_to_cognito_find
from clouday1_extract_aws_metadata.edge_lambda_sns_find import edge_lambda_sns_find
from clouday1_extract_aws_metadata.edge_transcribe_to_s3_find import edge_transcribe_to_s3_find
from clouday1_extract_aws_metadata.edge_lambda_to_sfn_find import edge_lambda_to_sfn_find
from clouday1_extract_aws_metadata.export_to_s3 import upload_to_S3,write_to_dynamo_db
from clouday1_extract_aws_metadata.rds_prepare_node import rds_prepare_node
from clouday1_extract_aws_metadata.ec2_prepare_node import ec2_prepare_node
from clouday1_extract_aws_metadata.resource_group_prepare_node import resource_group_prepare_node
from clouday1_extract_aws_metadata.resource_group_find_connection import rg_find_connection
from clouday1_extract_aws_metadata.webacl_prepare_node import waf_prepare_node
from clouday1_extract_aws_metadata.elbv2_prepare_node import elbv2_prepare_node
from clouday1_extract_aws_metadata.edge_waf_to_elbv2_find import edge_waf_to_elbv2_find
from clouday1_extract_aws_metadata.edge_elbv2_to_ec2_find import edge_elbv2_to_ec2_find


class Prepare:
    def __init__(self, region_name, account_id,cytoscape_node_data,cytoscape_edge_data):
        self.region_name = region_name
        self.account_id = account_id
        self.cytoscape_node_data = cytoscape_node_data
        self.cytoscape_edge_data = cytoscape_edge_data

    def exportToJSON(self):
        export_to_JSON(self.cytoscape_node_data, self.cytoscape_edge_data)

    def prepare_lambda_node(self):
        lambda_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_s3_node(self):
        s3_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_dynamodb_node(self):
        dynamodb_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_transcribe_node(self):
        transcribe_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_translate_node(self):
        translate_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

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
        cognito_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_ec2_node(self):
        ec2_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_rds_node(self):
        rds_prepare_node(self.region_name, self.account_id,
        self.cytoscape_node_data)

    def prepare_rg_node(self):
        resource_group_prepare_node(self.region_name,
        self.account_id, self.cytoscape_node_data)
    
    def prepare_waf_node(self):
        waf_prepare_node(self.region_name,self.account_id,
        self.cytoscape_node_data)

    def prepare_elbv2_node(self):
        elbv2_prepare_node(self.region_name,self.account_id,
        self.cytoscape_node_data)

    def find_sfn_connection(self):
        sfn_find_connection(self.cytoscape_node_data, self.cytoscape_edge_data)

    def find_edge_lambda_to_sns(self):
        edge_lambda_sns_find(self.cytoscape_edge_data, self.region_name)

    def find_edge_lambda_to_ddb(self):
        edge_lambda_ddb_find(self.cytoscape_edge_data, self.region_name)

    def find_edge_lambda_to_transcribe(self):
        edge_lambda_to_transcribe(self.cytoscape_edge_data, self.region_name, self.account_id)

    def find_edge_lambda_to_translate(self):
        edge_lambda_to_translate_find(self.cytoscape_edge_data, self.region_name,
        self.account_id)

    def find_edge_transcribe_to_s3(self):
        edge_transcribe_to_s3_find(self.cytoscape_edge_data, self.region_name,
        self.account_id)

    def find_edge_s3_to_cognito(self):
        edge_s3_to_cognito_find(self.cytoscape_edge_data)

    def find_edge_lambda_to_sfn(self):
        edge_lambda_to_sfn_find(self.region_name,self.cytoscape_edge_data)

    def find_edge_apigw_to_lambda(self):
        edge_apigw_to_lambda_find(self.cytoscape_edge_data, self.cytoscape_node_data)

    def find_edge_sns_to_lambda(self):
        edge_sns_to_lambda_find(self.cytoscape_edge_data)

    def rg_find_connection(self):
        rg_find_connection(self.cytoscape_node_data)

    def find_edge_waf_to_elb(self):
        edge_waf_to_elbv2_find(self.cytoscape_edge_data,self.cytoscape_node_data,
        self.region_name)
    
    def find_edge_elb_to_ec2(self):
        edge_elbv2_to_ec2_find(self.region_name,self.account_id,
        self.cytoscape_edge_data)

    def export_JSON_to_S3(self, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
        upload_to_S3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

    def write_to_dynamoDB(self, requestID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
        write_to_dynamo_db(requestID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
