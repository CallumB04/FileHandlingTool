import os
from mainmenu import mainmenu

def exitprog():
    print("Exiting File Handling Tool...")
    exit()

def main():
    
    cwd = os.path.dirname(os.getcwd())

    while True: 
        if mainmenu(cwd) == "exit":
            exitprog()


if __name__ == "__main__":
    main()