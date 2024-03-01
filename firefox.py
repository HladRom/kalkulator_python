#python

import subprocess

def open_firefox():
    try:
        subprocess.run(['firefox']) #This line attempts to run the Firefox application using the subprocess.run() function. It passes a list containing the command to run Firefox.
    except FileNotFoundError:
        print("Будь ласка, встановіть Firefox на своїй системі!")

if __name__ == "__main__":
    open_firefox()
    #open firefox!!!