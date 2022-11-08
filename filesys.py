import click

import read_files

@click.group()
@click.option("-e", "--environment", help='environment to run in', required=True,)
def cli(environment):
    click.echo(click.style(f"running in env: {environment}", fg="green"))

cli.add_command(read_files.read)