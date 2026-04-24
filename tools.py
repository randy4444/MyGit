import os
from pathlib import Path
import shutil


IGNORE = (".git", ".mygit", ".mygitignore", "mygit.py", ".gitignore", "git_commands.py", "tools.py")

def get_last_commit_id():
    lst = []
    for i in os.listdir(".mygit"):
        lst.append(int(i))
    
    if len(lst):
        return max(lst)
    
    return 0


def get_ignore():
    ignore = []
    with open(".mygitignore", "r", encoding="utf-8") as file:
        for i in file.readlines():
            ignore_path = Path(i.strip()).as_posix()
            ignore.append(ignore_path)

    return ignore


def delete_current():
    for i in os.listdir("."):
        if i not in IGNORE:
            if os.path.isdir(i):
                shutil.rmtree(i)
            else:
                os.remove(i)


def should_ignore(path, ignore):
    path = Path(path).as_posix()
    return path in ignore or path in IGNORE

    

def git_initialized():
    return os.path.exists(".mygit") and os.path.exists(".mygitignore")