import click

def generate_commit_message(path):
    if path:
        click.echo(f'Generating commit message for {path}...')
    else:
        click.echo(f'Generating commit message for current directory...')