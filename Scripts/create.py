import os, time, sys

def createfiles():
    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    print("=============================================================")
    print("                 -- File Creation Tool --                    ")
    print("=============================================================")

    print("\n    Type 'Exit' at any time to return to the main menu!    ")
    print("=============================================================")
    print("  State all the name[s] of the file[s] and file extention[s] ")
    print("   you would like to create, seperated into a list (, ) >>   ")
    print("\n     Files without an extension will be made as a .txt     ")
    print("=============================================================")
    files = str(input(">> "))

    if files == "" or files.upper() == "EXIT":
        return

    files = list(files)
    for i in range(0, len(files)):
        if files[i] == "," : files[i] = " "

    files = "".join(files).split("  ")

    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    while True:

        print("=============================================================")
        confirm = str(input(f"Are you sure you would like to create {len(files)} file[s] in the current directory: \n>> {os.path.dirname(os.getcwd())} \n\n[Y/N]"))

        if not confirm.upper() in ["Y", "N"]:
            if sys.platform == "win32" : os.system("cls")
            elif sys.platform == "linux" : os.system("clear")
            print("Invalid input. [Y/N]")

        if confirm.upper() == "Y":
            for filename in files:
                x = filename.find(".")

                if x == -1:
                    name = filename
                    ext = ".txt"

                else:
                    name = filename[:x]
                    ext = filename[x:]

                try: 
                    if sys.platform == "win32": filecreate = open(f"{os.path.dirname(os.getcwd())}\\{name}{ext}", "x")
                    elif sys.platform == "linux": filecreate = open(f"{os.path.dirname(os.getcwd())}/{name}{ext}", "x")
                except: pass

            if sys.platform == "win32" : os.system("cls")
            elif sys.platform == "linux" : os.system("clear")
            print("=============================================================")
            print(f"{len(files)} file[s] created in the current directory: \n>> {os.path.dirname(os.getcwd())}")
            print("=============================================================")
            print("\n")
            for i in range(0, 3):
                print(f"Returning to main menu in {3-i} second[s]!", end="\r")
                time.sleep(1)
            print("=============================================================")
            return 0

        elif confirm.upper() == "N":
            return

        
