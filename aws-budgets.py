import click

admin_email = click.prompt(
    click.style(
        "Please enter the email where you'd like budget notifications sent",
        bold=True),
    type=str)

click.echo("Sending notifications to %s" % click.style(admin_email, fg='green'))
