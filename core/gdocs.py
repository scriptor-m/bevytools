import click
from .utils import isGitInit

def generate_docs(path):
    if path:
        if isGitInit(path):
            click.echo(f'Generating docs for {path}...')
        else:
            click.echo(f'Path {path} is not a git repo. Please Intitialize git repo and try again.')
    else:
        if isGitInit('.'):
            click.echo(f'Generating docs for current directory...')
        else:
            click.echo(f'Current directory is not a git repo. Please Intitialize git repo and try again.')