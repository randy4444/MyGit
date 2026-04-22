import os
from tools import *


def init():
    if not git_initialized():
        os.mkdir(".mygit")
        file = open(".mygitignore", "x", encoding="utf-8")
        file.close()

def commit(message):
    pass

def checkout(id):
    pass