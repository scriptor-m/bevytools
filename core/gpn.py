import click

def generate_project_name(path):
    if path:
        click.echo(f'Generating project name for {path}...')
    else:
        click.echo(f'Generating project name for current directory...')