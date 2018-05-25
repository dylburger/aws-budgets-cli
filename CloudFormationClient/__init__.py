import boto3
from botocore.exceptions import ClientError
from pkg_resources import resource_filename

TEMPLATE_FILE = 'budgets.template.yaml'


def read_cf_template():
    filepath = resource_filename(__name__, TEMPLATE_FILE)
    with open(filepath, 'r') as f:
        return f.read()


def check_if_boto_response_is_successful(response):
    return response.get('ResponseMetadata', {}).get('HTTPStatusCode',
                                                    None) == 200


class CloudFormationClient():

    def __init__(self,
                 admin_email,
                 budget,
                 stack_name='aws-budgets',
                 profile=None):
        if profile:
            boto3.setup_default_session(profile_name=profile)

        self.client = boto3.client('cloudformation')
        self.stack_name = stack_name
        self.admin_email = admin_email
        self.budget = budget

    def _does_budget_stack_exist(self):
        # If this succeeds, the stack exists
        try:
            response = self.client.describe_stacks(StackName=self.stack_name)
            return check_if_boto_response_is_successful(response)
        # If the stack doesn't exist, boto throws this exception
        except ClientError:
            return False

    def create_stack(self):
        """ Creates CloudFormation stack for budgets, if it does not yet exist.
            Returns True if successful
        """
        if self._does_budget_stack_exist():
            print("%s CloudFormation stack already exists!" % self.stack_name)
            return False

        response = self.client.create_stack(
            StackName=self.stack_name,
            TemplateBody=read_cf_template(),
            Parameters=[{
                'ParameterKey': 'AdminEmail',
                'ParameterValue': self.admin_email,
            }, {
                'ParameterKey': 'BudgetThreshold',
                'ParameterValue': self.budget,
            }])

        if not check_if_boto_response_is_successful(response):
            print("Failed to create CloudFormation stack!")
            return False

        return response.get('StackId')
