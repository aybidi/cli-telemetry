import click
import sys

@click.command()
@click.option(
    "-fp",
    "--file-path",
    help='file path to read from',
    required=True,
)
def read(file_path):
    """
    read a file given its path
    """
    click.echo("reading files...")

    try:
        with open(file_path, "r") as f:
            content = f.read()
        click.echo(content)
    except FileNotFoundError:
        click.echo("sorry file not found")

    log_command(sys.argv)

def log_command(command):
    click.echo(command)