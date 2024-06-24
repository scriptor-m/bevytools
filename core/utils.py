from git import Repo
import ollama

def isGitInit(path):
    try:
        Repo(path)
        return True
    except:
        return False
    

