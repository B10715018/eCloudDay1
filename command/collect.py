from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function
from utils.sqs_list_queue import sqs_list_queue
from utils.sqs_get_queue import sqs_get_queue
from utils.sns_list_topic import sns_list_topic
from utils.sns_get_topic_attribute import sns_get_topic_attribute
from utils.dynamodb_list_table import dynamodb_list_table
from utils.dynamodb_scan import dynamodb_scan
from utils.cloudtrail_sfn_start_execution import cloudtrail_start_sfn
from utils.cloudtrail_translate_text import cloudtrail_translate_text
from utils.cloudtrail_start_transcription_job import cloudtrail_start_transcription_job
from utils.apigw_get_rest_apis import apigw_get_rest_apis
from utils.apigw_get_resources import apigw_get_resource
from utils.cloudtrail_waf_createWebACL import cloudtrail_waf_createWebACL
from utils.cloudwatch_describe_log_groups import cloudwatch_describe_log_groups
from utils.cloudwatch_describe_log_stream import cloudwatch_describe_log_stream
from utils.cloudwatch_get_log_event import cloudwatch_describe_log_event
from utils.s3_list_bucket import s3_list_bucket
from utils.s3_get_bucket_policy import s3_get_bucket_policy
from utils.rds_describe_instance import rds_describe_instance
from utils.elbv2_describe_load_balancer import elbv2_describe_load_balancer
from utils.elbv2_describe_target_group import elbv2_describe_target_group
from utils.elbv2_describe_target_health import elbv2_describe_target_health
from utils.ec2_describe_instances import ec2_describe_instances
from utils.ec2_describe_vpc_endpoint import ec2_describe_vpc_endpoint
from utils.ec2_describe_subnet import ec2_describe_subnets
from utils.ec2_describe_security_group import ec2_describe_security_group
from utils.ec2_describe_route_tables import ec2_describe_route_tables
from utils.ec2_describe_network_interfaces import ec2_describe_network_interfaces
from utils.ec2_describe_network_acls import ec2_describe_network_acls
from utils.ec2_describe_internet_gateway import ec2_describe_internet_gateway
from utils.ec2_describe_availability_zones import ec2_describe_availability_zone
from utils.sfn_list import sfn_list
from utils.sfn_describe import sfn_describe
from utils.waf_list_resource_web_acls import waf_list_resource_web_acl
from utils.apigw_get_integration import apigw_get_integration
from utils.cloudwatch_get_cognito_log_event import cloudwatch_get_cognito_log_event
from utils.cognito_list_identity_pool import cognito_list_identity_pool
from utils.s3_get_bucket_policy_status import s3_get_bucket_policy_status
from utils.dynamodb_describe_table import dynamodb_describe_table
from utils.cognito_describe_identity_pools import cognito_describe_identity_pools

'''Collect class for collecting data from AWS Services'''

REGION_NAME = 'us-west-2'


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name):
        self.region_name = region_name

    def get_lambda_list(self):
        lambda_list_function(self.region_name)

    def get_lambda_policy(self):
        lambda_get_policy(self.region_name)

    def list_sqs_queue(self):
        sqs_list_queue(self.region_name)

    def get_sqs_queue(self):
        sqs_get_queue(self.region_name)

    def list_sns_topic(self):
        sns_list_topic(self.region_name)

    def get_sns_topic_attribute(self):
        sns_get_topic_attribute(self.region_name)

    def list_dynamodb_table(self):
        dynamodb_list_table(self.region_name)

    def scan_dynamodb_table(self):
        dynamodb_scan(self.region_name)

    def get_cloudtrail_start_sfn(self):
        cloudtrail_start_sfn(self.region_name)

    def get_cloudtrail_translate_text(self):
        cloudtrail_translate_text(self.region_name)

    def get_cloudtrail_start_transcription_job(self):
        cloudtrail_start_transcription_job(self.region_name)

    def get_apigw_rest_apis(self):
        apigw_get_rest_apis(self.region_name)

    def get_apigw_resources(self):
        apigw_get_resource(self.region_name)

    def get_cloudtrail_waf_createWebACL(self):
        cloudtrail_waf_createWebACL(self.region_name)

    def get_cloudwatch_describe_log_groups(self):
        cloudwatch_describe_log_groups(self.region_name)

    def get_cloudwatch_describe_log_stream(self):
        cloudwatch_describe_log_stream(self.region_name)

    def get_cloudwatch_describe_log_event(self):
        cloudwatch_describe_log_event(self.region_name)

    def list_s3_bucket(self):
        s3_list_bucket(self.region_name)

    def get_s3_bucket_policy(self):
        s3_get_bucket_policy(self.region_name)

    def get_s3_bucket_policy_status(self):
        s3_get_bucket_policy_status(self.region_name)

    def describe_rds_instance(self):
        rds_describe_instance(self.region_name)

    def describe_elbv2_load_balancer(self):
        elbv2_describe_load_balancer(self.region_name)

    def describe_elbv2_target_group(self):
        elbv2_describe_target_group(self.region_name)

    def describe_elbv2_target_health(self):
        elbv2_describe_target_health(self.region_name)

    def describe_ec2_instances(self):
        ec2_describe_instances(self.region_name)

    def describe_ec2_vpc_endpoint(self):
        ec2_describe_vpc_endpoint(self.region_name)

    def describe_ec2_subnets(self):
        ec2_describe_subnets(self.region_name)

    def describe_ec2_security_groups(self):
        ec2_describe_security_group(self.region_name)

    def describe_ec2_route_tables(self):
        ec2_describe_route_tables(self.region_name)

    def describe_ec2_network_interfaces(self):
        ec2_describe_network_interfaces(self.region_name)

    def describe_ec2_network_acls(self):
        ec2_describe_network_acls(self.region_name)

    def describe_ec2_describe_availability_zones(self):
        ec2_describe_availability_zone(self.region_name)

    def describe_ec2_internet_gateway(self):
        ec2_describe_internet_gateway(self.region_name)

    def list_sfn(self):
        sfn_list(self.region_name)

    def describe_sfn(self):
        sfn_describe(self.region_name)

    def list_waf_web_acl(self):
        waf_list_resource_web_acl(self.region_name)

    def get_apigw_integration(self):
        apigw_get_integration(self.region_name)

    def get_cloudwatch_cognito_event(self):
        cloudwatch_get_cognito_log_event(self.region_name)

    def list_cognito_identity_pool(self):
        cognito_list_identity_pool(self.region_name)

    def describe_dynamodb_table(self):
        dynamodb_describe_table(self.region_name)

    def describe_cognito_identity_pools(self):
        cognito_describe_identity_pools(self.region_name)

# initialize class
collect_command = Collect(REGION_NAME)

# call command functions
collect_command.get_lambda_list()
collect_command.get_lambda_policy()
collect_command.list_sqs_queue()
collect_command.get_sqs_queue()
collect_command.list_sns_topic()
collect_command.get_sns_topic_attribute()
collect_command.list_dynamodb_table()
collect_command.scan_dynamodb_table()
collect_command.describe_dynamodb_table()
collect_command.get_cloudtrail_start_sfn()
collect_command.get_cloudtrail_translate_text()
collect_command.get_cloudtrail_start_transcription_job()
collect_command.get_apigw_rest_apis()
collect_command.get_apigw_resources()
collect_command.get_cloudtrail_waf_createWebACL()
collect_command.get_cloudwatch_describe_log_groups()
collect_command.get_cloudwatch_describe_log_stream()
collect_command.get_cloudwatch_describe_log_event()
collect_command.list_s3_bucket()
collect_command.get_s3_bucket_policy()
collect_command.describe_rds_instance()
collect_command.describe_elbv2_load_balancer()
collect_command.describe_elbv2_target_group()
collect_command.describe_elbv2_target_health()
collect_command.describe_ec2_instances()
collect_command.describe_ec2_vpc_endpoint()
collect_command.describe_ec2_subnets()
collect_command.describe_ec2_security_groups()
collect_command.describe_ec2_route_tables()
collect_command.describe_ec2_network_interfaces()
collect_command.describe_ec2_network_acls()
collect_command.describe_ec2_describe_availability_zones()
collect_command.describe_ec2_internet_gateway()
collect_command.list_sfn()
collect_command.describe_sfn()
collect_command.list_waf_web_acl()
collect_command.get_apigw_integration()
collect_command.get_cloudwatch_cognito_event()
collect_command.list_cognito_identity_pool()
collect_command.get_s3_bucket_policy_status()
collect_command.describe_cognito_identity_pools()