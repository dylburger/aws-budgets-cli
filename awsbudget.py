import click
from CloudFormationClient import CloudFormationClient


def generate_new_budget(admin_email, budget, profile):
    if admin_email is None:
        admin_email = click.prompt(
                click.style(
                    "Please enter the email address where you'd like budget notifications sent",
                    bold=True),
                type=str)

    click.echo(f'Sending notifications to {click.style(admin_email, fg="green")}')

    if budget is None:
        budget = click.prompt(
                click.style("Enter your budget in USD", bold=True), type=str)

    click.echo(f'Creating a new budget of {click.style("$" + budget, fg="green")}')

    # Create a new CloudFormation client to manage budgets
    cfclient = CloudFormationClient(admin_email, budget, profile=profile)
    stackid = cfclient.create_stack()
    if stackid:
        click.echo(f'Created CloudFormation stack to manage budgets: {stackid}')


@click.command()
@click.option('--new', '-n', is_flag=True, help="Create a new AWS budget")
@click.option('--admin_email', '-e', default=None, help="The email address to which budget notifications are sent")
@click.option('--budget', '-b', default=None, help="The budget (in USD) you want to set")
@click.option('--profile', '-p', default=None, help="AWS profile name")
def cli(new, admin_email, budget, profile):
    if new is True:
        generate_new_budget(admin_email, budget, profile)
        return
