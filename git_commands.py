import os
from tools import *


def init():
    if not git_initialized():
        os.mkdir(".mygit")
        file = open(".mygitignore", "x", encoding="utf-8")
        file.close()
    else:
        print("Репозиторий уже создан")

def commit(message):
    commit_id = get_last_commit_id() + 1
    commit_path = os.path.join(".mygit", str(commit_id))
    os.mkdir(commit_path)
    meesage_path = os.path.join(commit_path, ".message.txt")
    with open(meesage_path, "x", encoding="utf-8") as message_file:
        message_file.write(message)

    ignore = get_ignore()
    for i in os.walk("."):
        current, dirs, files = i

        if should_ignore(current, ignore):
            dirs.clear()
            continue
        
        if current != ".":
            os.mkdir(os.path.join(commit_path, current))

        for dir in dirs:
            if current != ".":
                dir_path = os.path.join(current, dir)
            else:
                dir_path = dir

            if should_ignore(dir_path, ignore):
                dirs.remove(dir)

        for file in files:
            if current != ".":
                file_path = os.path.join(current, file)
            else:
                file_path = file

            if not should_ignore(file_path, ignore):
                save_path = os.path.join(commit_path, file_path)
                f = open(save_path, "x", encoding="utf-8")
                f.close()


def checkout(id):
    pass