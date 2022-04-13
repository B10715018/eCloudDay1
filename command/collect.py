from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function

'''Collect class for collecting data from AWS Lambda'''


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name):
        self.region_name = region_name

    def get_lambda_list(self):
        lambda_list_function()

    def get_lambda_policy(self):
        lambda_get_policy()


# initialize class
collect_command = Collect('us-west-2')

collect_command.get_lambda_list()
collect_command.get_lambda_policy()
