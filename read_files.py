import click
import sys

from bq_storage import upload_data

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
    sanitized_command = sanitize_command(command)
    upload_data(sanitized_command)

def sanitize_command(command) -> str:
    """
    makes sure to clean the command of any secrets
    before logging
    """
    if not command:
        return
    first_word = command[0].split("/")[-1]
    final_command = " ".join([first_word] + command[1:])
    return final_command
