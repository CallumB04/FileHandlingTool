import os
from rename import renamefiles
from delete import deletefiles
from create import createfiles

def mainmenu(cwd):
    os.system("cls")

    print("=============================================================")
    print(f"What would you like to do in the current directory ({cwd})")
    print("1. Rename Files")
    print("2. Delete Files")
    print("3. Create Files")
    print("4. Exit")
    print("=============================================================")
    choice = str(input())

    if choice == "1" or choice.upper() == "RENAME" : renamefiles(cwd)
    elif choice == "2" or choice.upper() == "DELETE" : deletefiles(cwd)
    elif choice == "3" or choice.upper() == "CREATE" : createfiles(cwd)
    elif choice == "4" or choice.upper() == "EXIT" : return "exit"
    else: print("--- Not an option! Try again! ---")

    return 0
