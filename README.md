## awsbudget

`awsbudget` is a small, Python command-line utility for creating simple [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/).

At the moment, this tool was built to solve a very simple use case - you want to create a *single* budget in USD, with notifications at three levels:

* You are _projected_ to spend greater than 80% of your budget
* You have spent greater than 70% of your budget
* You've spent 100% of your budget

and you want these notifications to go directly to an email address (vs. to an SNS topic).

Behind the scenes, we create a CloudFormation stack using the [template in this repo](templates/budgets.template.yaml) to manage this budget in the default region tied to your account.

**This tool uses [boto3](https://github.com/boto/boto3) to make requests to AWS**. If you're having trouble authenticating to the correct account, note that `boto3` looks for your AWS credentials and profile information in [a few different places](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

#### Installation

Within your target Python virtual environment, run

    pip install awsbudget

or `git clone` this repository, then from the root of the repo, run

    pip install .

#### Usage

Run `awsbudget --help` to get a full list of options.

You can create a budget by passing all required data as command line options directly:

    awsbudget --new --admin_email admin@host.com --budget 20    

or you can run

    awsbudget --new

and the tool will prompt you for the data interactively:

    $ awsbudget --new --profile personal
    Please enter the email address where you'd like budget notifications sent: admin@host.com
    Sending notifications to admin@host.com
    Enter your budget in USD: 20
    Creating a new budget of $20
    Created CloudFormation stack to manage budgets: arn:aws:cloudformation:us-east-1:account-id:stack/aws-budgets/stack-id

Note that you can specify that `awsbudget` use a specific AWS profile defined in your AWS config file (e.g. `~/.aws/config`). 

    awsbudget --new --profile personal

This can be useful when creating budgets for multiple AWS accounts.

