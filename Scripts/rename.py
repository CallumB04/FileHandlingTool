import os, sys, time

## bulk renaming not implemented yet
def renamefiles():
    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    print("=============================================================")
    print("                 -- File Renaming Tool --                    ")
    print("=============================================================")

    print("\n    Type 'Exit' at any time to return to the main menu!    ")
    print("=============================================================")
    print("       State the name of a file and its file extention       ")
    print("                  you would like to rename!                  ")
    print("=============================================================")
    file = str(input(">> "))

    if file.upper() == "EXIT":
        return

    if sys.platform == "win32" : os.system("cls")
    elif sys.platform == "linux" : os.system("clear")

    while True:
        print("=============================================================")
        newFile = str(input(f"What would you like to rename the file '{file}' to? >> "))

        if sys.platform == "win32" : os.system("cls")
        elif sys.platform == "linux" : os.system("clear")

        try:   
            
            x = newFile.find(".")

            if x == -1:
                name = newFile
                ext = file[file.find("."):]
            
            else:
                name = newFile[:x]
                ext = newFile[x:]

            if sys.platform == "win32": os.rename(f"{os.path.dirname(os.getcwd())}\\{file}", f"{os.path.dirname(os.getcwd())}\\{name}{ext}")
            elif sys.platform == "linux": os.rename(f"{os.path.dirname(os.getcwd())}/{file}", f"{os.path.dirname(os.getcwd())}/{name}{ext}")
            
            print("=============================================================")
            print(f"Old file name >> {file}\nNew File name {name}{ext}")
            print("=============================================================")
            print("\n")

            for i in range(0, 3):
                print(f"Returning to main menu in {3-i} second[s]!", end="\r")
                time.sleep(1)
            print("=============================================================")
            return 0

        except:
            for i in range(1, 4): 
                print(f"File name: {file} doesnt exist / couldnt be renamed, returning to main menu", "."*i, end="\r")
                time.sleep(1)
 
            return

    return