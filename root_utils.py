import ollama
import json

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








