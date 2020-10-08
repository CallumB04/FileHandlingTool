import os, sys
from rename import renamefiles
from delete import deletefiles
from create import createfiles

def mainmenu():
    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    print("=============================================================")
    print(f"What would you like to do in the current directory ({os.path.dirname(os.getcwd())})")
    print("1. Rename Files")
    print("2. Delete Files")
    print("3. Create Files")
    print("4. Exit")
    print("=============================================================")
    choice = str(input())

    if choice == "1" or choice.upper() == "RENAME" : renamefiles()
    elif choice == "2" or choice.upper() == "DELETE" : deletefiles()
    elif choice == "3" or choice.upper() == "CREATE" : createfiles()
    elif choice == "4" or choice.upper() == "EXIT" : return "exit"
    else: print("--- Not an option! Try again! ---")

    return 0
