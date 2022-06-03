from clouday1_extract_aws_metadata.lambda_list_function import lambda_list_function
from clouday1_extract_aws_metadata.lambda_get_policy import lambda_get_policy
from clouday1_extract_aws_metadata.sqs_list_queue import sqs_list_queue
from clouday1_extract_aws_metadata.sqs_get_queue import sqs_get_queue
from clouday1_extract_aws_metadata.sns_list_topic import sns_list_topic
from clouday1_extract_aws_metadata.sns_get_topic_attribute import sns_get_topic_attribute
from clouday1_extract_aws_metadata.dynamodb_list_table import dynamodb_list_table
from clouday1_extract_aws_metadata.dynamodb_scan import dynamodb_scan
from clouday1_extract_aws_metadata.cloudtrail_sfn_start_execution import cloudtrail_start_sfn
from clouday1_extract_aws_metadata.cloudtrail_translate_text import cloudtrail_translate_text
from clouday1_extract_aws_metadata.cloudtrail_start_transcription_job import cloudtrail_start_transcription_job
from clouday1_extract_aws_metadata.apigw_get_rest_apis import apigw_get_rest_apis
from clouday1_extract_aws_metadata.apigw_get_resources import apigw_get_resource
from clouday1_extract_aws_metadata.cloudtrail_waf_createWebACL import cloudtrail_waf_createWebACL
from clouday1_extract_aws_metadata.cloudwatch_describe_log_groups import cloudwatch_describe_log_groups
from clouday1_extract_aws_metadata.cloudwatch_describe_log_stream import cloudwatch_describe_log_stream
from clouday1_extract_aws_metadata.cloudwatch_get_log_event import cloudwatch_describe_log_event
from clouday1_extract_aws_metadata.s3_list_bucket import s3_list_bucket
from clouday1_extract_aws_metadata.s3_get_bucket_policy import s3_get_bucket_policy
from clouday1_extract_aws_metadata.s3_get_bucket_policy_status import s3_get_bucket_policy_status
from clouday1_extract_aws_metadata.rds_describe_instance import rds_describe_instance
from clouday1_extract_aws_metadata.elbv2_describe_load_balancer import elbv2_describe_load_balancer
from clouday1_extract_aws_metadata.elbv2_describe_target_group import elbv2_describe_target_group
from clouday1_extract_aws_metadata.elbv2_describe_target_health import elbv2_describe_target_health
from clouday1_extract_aws_metadata.elbv2_list_tags import elb_list_tags
from clouday1_extract_aws_metadata.ec2_describe_instances import ec2_describe_instances
from clouday1_extract_aws_metadata.ec2_describe_vpc_endpoint import ec2_describe_vpc_endpoint
from clouday1_extract_aws_metadata.ec2_describe_subnet import ec2_describe_subnets
from clouday1_extract_aws_metadata.ec2_describe_security_group import ec2_describe_security_group
from clouday1_extract_aws_metadata.ec2_describe_route_tables import ec2_describe_route_tables
from clouday1_extract_aws_metadata.ec2_describe_network_interfaces import ec2_describe_network_interfaces
from clouday1_extract_aws_metadata.ec2_describe_network_acls import ec2_describe_network_acls
from clouday1_extract_aws_metadata.ec2_describe_availability_zones import ec2_describe_availability_zone
from clouday1_extract_aws_metadata.ec2_describe_internet_gateway import ec2_describe_internet_gateway
from clouday1_extract_aws_metadata.sfn_list import sfn_list
from clouday1_extract_aws_metadata.sfn_describe import sfn_describe
from clouday1_extract_aws_metadata.waf_list_resource_web_acls import waf_list_resource_web_acl
from clouday1_extract_aws_metadata.apigw_get_integration import apigw_get_integration
from clouday1_extract_aws_metadata.cloudwatch_get_cognito_log_event import cloudwatch_get_cognito_log_event
from clouday1_extract_aws_metadata.dynamodb_describe_table import dynamodb_describe_table
from clouday1_extract_aws_metadata.cognito_list_identity_pool import cognito_list_identity_pool
from clouday1_extract_aws_metadata.cognito_describe_identity_pools import cognito_describe_identity_pools
from clouday1_extract_aws_metadata.sns_list_tags import sns_list_tags
from clouday1_extract_aws_metadata.sfn_list_tags import sfn_list_tags
from clouday1_extract_aws_metadata.dynamodb_list_tags_of_resource import ddb_list_tags_of_resource
from clouday1_extract_aws_metadata.s3_get_bucket_tagging import s3_get_bucket_tagging
from clouday1_extract_aws_metadata.lambda_list_tags import lambda_list_tags
from clouday1_extract_aws_metadata.resource_group_list_groups import resource_group_list_groups
from clouday1_extract_aws_metadata.resource_group_list_group_resources import resource_group_list_group_resources
from clouday1_extract_aws_metadata.resource_group_list_tags import resource_group_get_tags
from clouday1_extract_aws_metadata.wafv2_list import wafv2_list_web_acl
from clouday1_extract_aws_metadata.waf_list_tags import waf_list_tags
'''Collect class for collecting data from AWS Services'''


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name, account_id, aws_access_key_id, aws_secret_access_key):
        self.region_name = region_name
        self.account_id = account_id
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def get_lambda_list(self):
        lambda_list_function(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_lambda_policy(self):
        lambda_get_policy(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_sqs_queue(self):
        sqs_list_queue(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_sqs_queue(self):
        sqs_get_queue(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_sns_topic(self):
        sns_list_topic(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_sns_topic_attribute(self):
        sns_get_topic_attribute(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_dynamodb_table(self):
        dynamodb_list_table(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def scan_dynamodb_table(self):
        dynamodb_scan(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudtrail_start_sfn(self):
        cloudtrail_start_sfn(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudtrail_translate_text(self):
        cloudtrail_translate_text(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudtrail_start_transcription_job(self):
        cloudtrail_start_transcription_job(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_apigw_rest_apis(self):
        apigw_get_rest_apis(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_apigw_resources(self):
        apigw_get_resource(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudtrail_waf_createWebACL(self):
        cloudtrail_waf_createWebACL(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudwatch_describe_log_groups(self):
        cloudwatch_describe_log_groups(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudwatch_describe_log_stream(self):
        cloudwatch_describe_log_stream(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudwatch_describe_log_event(self):
        cloudwatch_describe_log_event(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_s3_bucket(self):
        s3_list_bucket(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_s3_bucket_policy(self):
        s3_get_bucket_policy(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_s3_bucket_policy_status(self):
        s3_get_bucket_policy_status(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_rds_instance(self):
        rds_describe_instance(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_elbv2_load_balancer(self):
        elbv2_describe_load_balancer(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_elbv2_target_group(self):
        elbv2_describe_target_group(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_elbv2_target_health(self):
        elbv2_describe_target_health(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_elb_tags(self):
        elb_list_tags(self.region_name,self.aws_access_key_id,
        self.aws_secret_access_key)

    def describe_ec2_instances(self):
        ec2_describe_instances(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_vpc_endpoint(self):
        ec2_describe_vpc_endpoint(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_subnets(self):
        ec2_describe_subnets(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_security_groups(self):
        ec2_describe_security_group(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_route_tables(self):
        ec2_describe_route_tables(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_network_interfaces(self):
        ec2_describe_network_interfaces(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_network_acls(self):
        ec2_describe_network_acls(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_describe_availability_zones(self):
        ec2_describe_availability_zone(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_ec2_internet_gateway(self):
        ec2_describe_internet_gateway(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_sfn(self):
        sfn_list(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_sfn(self):
        sfn_describe(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)
    def list_waf_web_acl(self):
        wafv2_list_web_acl(self.region_name,self.aws_access_key_id,
        self.aws_secret_access_key)

    def list_waf_tags(self):
        waf_list_tags(self.region_name,self.aws_access_key_id,
        self.aws_secret_access_key)

    def list_waf_resource(self):
        waf_list_resource_web_acl(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_apigw_integration(self):
        apigw_get_integration(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def get_cloudwatch_cognito_event(self):
        cloudwatch_get_cognito_log_event(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_cognito_identity_pool(self):
        cognito_list_identity_pool(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_dynamodb_table(self):
        dynamodb_describe_table(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def describe_cognito_identity_pools(self):
        cognito_describe_identity_pools(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_sns_tag(self):
        sns_list_tags(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_sfn_tag(self):
        sfn_list_tags(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_ddb_tag(self):
        ddb_list_tags_of_resource(self.region_name,
        self.account_id, self.aws_access_key_id, self.aws_secret_access_key)

    def list_s3_tag(self):
        s3_get_bucket_tagging(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_lambda_tag(self):
        lambda_list_tags(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_resource_group(self):
        resource_group_list_groups(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)

    def list_resource_group_resources(self):
        resource_group_list_group_resources(
            self.region_name, self.aws_access_key_id, self.aws_secret_access_key
        )

    def list_resource_group_tag(self):
        resource_group_get_tags(self.region_name,
        self.aws_access_key_id, self.aws_secret_access_key)
