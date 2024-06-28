import click
import sqlite3
from .utils import give_cursor , zip_directory
import os
from .loader import Loader
import time


def list_all_templates():
    cursor , conn = give_cursor()
    cursor.execute('SELECT * FROM templates')
    # fetch all the rows
    rows = cursor.fetchall()
    # if the rows are empty, echo a message
    if not rows:
        click.echo('No templates found')
        return
    click.echo(rows)


def create_new_template(name : str , path : str):
    cursor , conn = give_cursor()
    # if the template name already exists, return -1 
    cursor.execute('SELECT * FROM templates WHERE name = ?', (name,))
    if cursor.fetchone():
        click.echo(f'Template with name {name} already exists')
        return -1
    # if the either of s_path or d_path does not exist, echo a message and return -1
    if not path:
        click.echo('Both source and destination paths are required')
        return -1
    # check whether the paths exist or not 
    if not os.path.exists(path):
        click.echo('Both source and destination paths must exist')
        return -1
    # create the template
    cursor.execute('INSERT INTO templates (name, path) VALUES (?, ? )', (name, path))
    click.echo('zipping source code...')
    Loader().start()
    try:
        zip_directory(name, path)
    except Exception as e:
        Loader().stop()
        click.echo("\nError :" , e)
        return
    finally:
        Loader().stop()
    conn.commit()
    click.echo(f'Template {name} created successfully')


def load_template():
    click.echo('Load template option')


def search_template():
    click.echo('Search template option')


def delete_template():
    click.echo('Delete template option')

