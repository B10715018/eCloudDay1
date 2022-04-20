import os
import boto3
import json


def cognito_describe_identity_pools(region):
    script_dir = os.path.dirname('.')
    file_path_read_cognito_list = os.path.join(
        script_dir, 'data/cognito-list-identity-pools-'+region+'.json')
    with open(file_path_read_cognito_list, 'r') as
