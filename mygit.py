import sys
from git_commands import *


if len(sys.argv) <= 1:
    print(sys.argv)
    print("Недостаточное количество аргументов")
else:
    command_name = sys.argv[1]
    if command_name == "init":
        if len(sys.argv) != 2:
            print("Неверное использование команды init")
        else:
            init()
    elif command_name == "commit":
        if len(sys.argv) != 3:
            print("неверное использование команды commit")
        else:
            message = sys.argv[2]
            commit(message)
    elif command_name == "checkout":
        if len(sys.argv) != 3:
            print("неверное использование команды checkout")
        else:
            id = sys.argv[2]
            checkout(id)
    else:
        print(f"Неизвестная команда: '{command_name}'")