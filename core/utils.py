from git import Repo

def isGitInit(path):
    try:
        Repo(path)
        return True
    except:
        return False
    

