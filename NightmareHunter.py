from pineappledev.pineappledev import *
import os
def nhlogo():
    print("""\x1b[0;31m
\x1b[0;36m ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓ ███▄ ▄███▓ ▄▄▄       ██▀███  ▓█████\x1b[0;31m  ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
\x1b[0;36m ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀\x1b[0;31m ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
\x1b[0;36m▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███  \x1b[0;31m ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
\x1b[0;36m▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄\x1b[0;31m ░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
\x1b[0;36m▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒░▒████\x1b[0;31m▒░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
\x1b[0;36m░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ \x1b[0;31m ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
\x1b[0;36m░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ ▒ ░\x1b[0;31m▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
\x1b[0;36m   ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      ░      ░     ░   ▒     ░░   ░    ░    ░  ░░\x1b[0;31m ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
\x1b[0;36m         ░  ░        ░  ░  ░  ░                ░         ░  ░   ░        ░  ░ ░  ░  ░\x1b[0;31m   ░              ░             ░  ░   ░     
    \x1b[0;31m
#################################################################
                            \x1b[0;34mBy x04000
                    \x1b[0;33mGithub: github.com/x04000
                    \x1b[0;32mBase: Python, PineappleDev
                          \x1b[0;36mVersion: 0.1
\x1b[0;31m#################################################################
\x1b[0;35m
    """)
def nhclear():
    try:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    except:
        print("")
nhclear()
nhlogo()
def nhinst():
    try:
        while(True):
            print("\x1b[1;36m┌──(\x1b[1;31mroot@\x1b[1;0mNightmareHunter\x1b[1;36m)-\x1b[1;36m[\x1b[1;29m~\x1b[1;36m]")
            nhinst = str(input("\x1b[1;36m└─$ \x1b[0;31m"))
            if nhinst == "exit":
                break
            if nhinst == "clear":
                nhclear()
            if nhinst == "autoinst":
                try:
                    if os.path.isdir("PineappleKiller"):
                        print("You have got installed: PineappleKiller !")
                    else:
                        os.system("sudo apt-get install git")
                        os.system("git clone https://github.com/x04000/PineappleKiller")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if nhinst == "update":
                try:
                    os.system("sudo apt-get install git")
                    if os.path.isdir("PineappleKiller"):
                        os.system("sudo rm -rfv PineappleKiller")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if nhinst == "inst PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    print("You have got installed: PineappleKiller !")
                else:
                    os.system("sudo apt-get install git")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
            if nhinst == "update PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    os.system("sudo apt-get install git")
                    os.system("sudo rm -rfv PineappleKiller")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
                else:
                    print("You havent got installed: PineappleKiller !")
            if nhinst == "remove PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    os.system("sudo rm -rfv PineappleKiller")
                else:
                    print("You havent got installed: PineappleKiller !")
    except:
        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
try:
    while(True):
        print("\x1b[1;36m┌──(\x1b[1;31mHunter💀NightmareHunter\x1b[1;36m)-\x1b[1;36m[\x1b[1;29m~/NightmareHunter\x1b[1;36m]")
        nhi = str(input("\x1b[1;36m└─$ \x1b[0;31m"))
        if nhi == "exit":
            print("\x1b[1;32mHave a good day :)")
            break
        if nhi == "clear":
            nhclear()
        if nhi == "nhinst":
            nhclear()
            nhlogo()
            nhinst()
        else:
            try:
                os.system(nhi)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
except:
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")