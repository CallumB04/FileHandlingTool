import os, time

def deletefiles():
    try : os.system("cls")
    except : os.system("clear")
    deletedcount = 0

    print("=============================================================")
    print("                 -- File Deletion Tool --                    ")
    print("=============================================================")
    
    print("\n    Type 'Exit' at any time to return to the main menu!    ")
    print("=============================================================")
    print("  State all the name[s] of the file[s] and file extention[s] ")
    print("  you would like to delete, seperated using a comma (, ) >>  ")
    print("\n     Files without an extension will not be deleted!       ")
    print("=============================================================")
    files = str(input(">> "))

    if files == "" or files.upper() == "EXIT":
        return

    files = list(files)
    for i in range(0, len(files)):
        if files[i] == "," : files[i] = " "

    files = "".join(files).split("  ")

    try : os.system("cls")
    except : os.system("clear")

    while True:

        print("=============================================================")
        confirm = str(input(f"Are you sure you would like to delete {len(files)} file[s] in the current directory: \n>> {os.path.dirname(os.getcwd())} \n\n[Y/N]"))

        if not confirm.upper() in ["Y", "N"]:
            try : os.system("cls")
            except : os.system("clear")
            print("Invalid input. [Y/N]")

        if confirm.upper() == "Y":
            for filename in files:
                x = filename.find(".")

                if x == -1:
                    name = filename
                    ext = ""

                else:
                    name = filename[:x]
                    ext = filename[x:]

                try: 
                    if ext != "":
                        os.remove(f"{os.path.dirname(os.getcwd())}\\{name}{ext}")
                        deletedcount += 1
                except: pass

            try : os.system("cls")
            except : os.system("clear")
            print("=============================================================")
            print(f"{deletedcount} file[s] deleted in the current directory: \n>> {os.path.dirname(os.getcwd())}")
            print("=============================================================")
            print("\n")
            for i in range(0, 3):
                print(f"Returning to main menu in {3-i} second[s]!", end="\r")
                time.sleep(1)
            print("=============================================================")
            return 0

        elif confirm.upper() == "N":
            return

        