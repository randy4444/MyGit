import os

def get_last_commit_id():
    lst = []
    for i in os.listdir(".mygit"):
        lst.append(int(i))
    
    if len(lst):
        return max
    
    return 1


def git_initialized():
    return os.path.exists(".mygit") and os.path.exists(".mygitignore")