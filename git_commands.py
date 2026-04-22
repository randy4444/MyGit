import os


def init():
    if not os.path.exists(".mygit"):
        os.mkdir(".mygit")
        file = open(".mygitignore", "x", encoding="utf-8")
        file.close()

def commit(message):
    pass

def checkout(id):
    pass