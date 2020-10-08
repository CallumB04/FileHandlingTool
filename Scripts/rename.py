import os, sys

def renamefiles():
    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    print("=============================================================")
    print("                 -- File Renaming Tool --                    ")
    print("=============================================================")

    return