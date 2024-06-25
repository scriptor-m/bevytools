import asyncio
import ollama
import json
from core.loader import Loader
from git import Repo

config_data = {
    'ollama_model' : '',
    'ollama_server_url' : '',
}

def load_config():
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        with open('config.json', 'w') as config_file:
            json.dump(config_data, config_file)
            return config_data

def save_config(config):
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)



def check_ollama():
    content = ""
    with open('template.txt' , 'r') as data:
        content = data.read()
    
    config = load_config()
    
    try : 
        stream = ollama.chat(
            model=config['ollama_model'],
            messages=[{'role': 'user', 'content': content}],
            stream=True,
        )
    except Exception as e:
        print("error connecting with ollama server.")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)




def check_changes():
    repo = Repo('.')
    print(repo.git.diff(repo.commit("HEAD")))












