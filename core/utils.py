from git import Repo
import ollama
import sqlite3
import zipfile
import os
import hashlib

db_name = 'data.db'
exception_dir = 'bt_templates'

def isGitInit(path):
    try:
        Repo(path)
        return True
    except:
        return False
    
def give_cursor():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS templates (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, path TEXT NOT NULL )')
    return (cursor , conn)

def zip_directory( name ,directory_path=None):
    # Determine the directory to zip
    if directory_path is None:
        directory_path = os.getcwd()
    
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.getcwd(), exception_dir)
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
    
    # Path to the output zip file
    output_zip = os.path.join(templates_dir, f'{name}.zip')
    
    # Zip the files
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, dirs, files in os.walk(directory_path):
            # ignore templates directory
            # ignore the files with .db-journal and .db-wal
            # if any
            if exception_dir in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname)
            for file in files:
                if file.endswith('.db-journal') or file.endswith('.db-wal'):
                    files.remove(file)
            


