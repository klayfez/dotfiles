import subprocess, sys

def get_status():
    zapret_status = subprocess.run(["systemctl", "status", "zapret"], capture_output=True, text=True).stdout
    zapret_status = zapret_status.splitlines()
    for i in zapret_status:
        if "Active:" in i:
            return i.split()[1]

def turn_zapret():
    if get_status() == "inactive":
        subprocess.run(["systemctl","start","zapret"])
    elif get_status() == "active":
        subprocess.run(["systemctl", "stop", "zapret"])

def main():
    arg = sys.argv[1]
    if arg == "status":
        print("zapret:", get_status())
    elif arg == "turn":
        turn_zapret()
        
if __name__ == "__main__":
    main()