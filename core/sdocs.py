import click

def serve_docs(path , port):
    if path:
        click.echo(f'Serving docs for {path}...')
    else:
        click.echo(f'Serving docs for current directory...')