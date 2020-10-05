import os
from mainmenu import mainmenu

def exitprog():
    print("Exiting File Handling Tool...")
    exit()

def main():

    while True: 
        if mainmenu() == "exit":
            exitprog()


if __name__ == "__main__":
    main()