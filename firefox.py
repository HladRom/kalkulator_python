#python
import subprocess

def open_firefox():
    try:
        subprocess.run(['firefox'])
    except FileNotFoundError:
        print("Будь ласка, встановіть Firefox на своїй системі!")

if __name__ == "__main__":
    open_firefox()
    #open firefox!!!