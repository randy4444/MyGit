import os
from tools import *


COMMIT_MESSAGE_NAME = ".hidden_message.txt"


def init():
    if not os.path.exists(".mygitignore"):
        os.mkdir(".mygit")
        file = open(".mygitignore", "x", encoding="utf-8")
        file.close()
    else:
        print("Репозиторий уже создан")

def commit(message):
    if COMMIT_MESSAGE_NAME in os.listdir("."):
        print(f"Запрщено создавать файл {COMMIT_MESSAGE_NAME} в директории '.'")
        return

    commit_id = get_last_commit_id() + 1
    commit_path = os.path.join(".mygit", str(commit_id))
    os.mkdir(commit_path)
    message_path = os.path.join(commit_path, COMMIT_MESSAGE_NAME)
    with open(message_path, "x", encoding="utf-8") as message_file:
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
                print(file_path)
                with open(file_path, "rb") as read_file:
                    data = read_file.read()

                save_path = os.path.join(commit_path, file_path)
                with open(save_path, "ab") as save_file:
                    save_file.write(data)


def checkout(id):
    commit_path = os.path.join(".mygit", str(id))
    if not os.path.exists(commit_path):
        print(f"Коммит с id = {id} не существует")
        return
    message_file_path = os.path.join(commit_path, COMMIT_MESSAGE_NAME)
    with open(message_file_path, "rb") as message_file:
        message = message_file.read().decode("utf-8")

    print(f"Коммит {id}. Сообщение: '{message}'")
    delete_current()
    for i in os.walk(commit_path):
        current, dirs, files = i

        if current != commit_path:
            current_rel_path = os.path.relpath(current, commit_path)
            os.mkdir(current_rel_path)
        
        for file in files:
            if file == COMMIT_MESSAGE_NAME:
                continue

            if current != commit_path:
                file_path = os.path.join(current, file)
            else:
                file_path = os.path.join(commit_path, file)

            with open(file_path, "rb") as file:
                data = file.read() 

            save_path = os.path.relpath(file_path, commit_path)
            with open(save_path, "ab") as save_file:
                save_file.write(data)