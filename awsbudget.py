import click
from CloudFormationClient import CloudFormationClient


def generate_new_budget(profile):
    admin_email = click.prompt(
            click.style(
                "Please enter the email address where you'd like budget notifications sent",
                bold=True),
            type=str)
    click.echo(
            f'Sending notifications to {click.style(admin_email, fg="green")}')

    budget = click.prompt(
            click.style("Enter your budget in USD", bold=True), type=str)
    click.echo(f'Creating a new budget of {click.style("$" + budget, fg="green")}')

    # Create a new CloudFormation client to manage budgets
    cfclient = CloudFormationClient(admin_email, budget, profile=profile)
    stackid = cfclient.create_stack()
    if stackid:
        click.echo(f'Created CloudFormation stack to manage budgets: {stackid}')



@click.command()
@click.option('--list_budgets', is_flag=True, help="List any existing budgets")
@click.option('--new', is_flag=True, help="Create a new AWS budget")
@click.option('--profile', '-p', default=None, help="AWS profile name")
def cli(list_budgets, new, profile):
    if list_budgets is True:
        click.echo("Listing budgets here")
        return

    if new is True:
        generate_new_budget(profile)
        return
