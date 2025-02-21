#python
import subprocess

def open_firefox():
    try:
        subprocess.run(['firefox'])
    except FileNotFoundError:
        print("install Firefox!")

if __name__ == "__main__":
    open_firefox()
    #open firefox!!!