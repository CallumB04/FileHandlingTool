import os

def createfiles(cwd):
    os.system("cls")

    print("=============================================================")
    print("                 -- File Creation Tool --                    ")
    print("=============================================================")

    print("Type 'Exit' at any time to return to the main menu!")
    print("State all the name[s] of the file[s] you would like to create,")
    print("seperated using a comma (, ) >>")
    print("=============================================================")
    files = str(input())

    if files == "" or files.upper() == "EXIT":
        return

    files = list(files)
    for i in range(0, len(files)):
        if files[i] == "," : files[i] = " "

    files = "".join(files).split("  ")
    
    os.system("cls")

    print("=============================================================")
    confirm = str(input(f"Are you sure you would like to create {len(files)} file[s] in the current directory: \n>> {cwd} \n\n[Y/N]"))
   
    ## open("<filename.extension>", "x") to create files