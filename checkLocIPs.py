import requests
import subprocess
import re
import json
import time
from colorama import Fore, Back, Style, init
import socket

def check_ip_reputation(ip_address):
    url = f"https://www.spamhaus.org/query/ip/{ip_address}"
    response = requests.get(url)
    if "not listed" in response.text:
        return True
    else:
        return False
    
SAVEHOST = ["Microsoft", "Amazon", "Google"]

# Hole den Hostnamen deines Computers
hostname = socket.gethostname()

# Initialisiere colorama
init(autoreset=True)

# Hole die IP-Adresse, die diesem Hostnamen zugeordnet ist
token = input("Please enter your ipinfo.io api token: ")
myIP = socket.gethostbyname(hostname)
localhost = "127.0.0.1"

# Führe den netstat-Befehl aus und erfasse den Output zeilenweise
process = subprocess.Popen(
    ['netstat', '-a', '-n'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Erfasse und verarbeite die Ausgabe zeilenweise
for line in process.stdout:
    # Der Regex-Ausdruck, um nach IP-Adressen zu suchen
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    # Suche nach IP-Adressen im Text
    ip_addresses = re.findall(ip_pattern, line.strip())

    # Gib die gefundenen IP-Adressen aus
    for ip in ip_addresses:
        if ip == "0.0.0.0" or ip == myIP or ip == localhost:
            continue
        else:
            isLegit = check_ip_reputation(ip)
            res =requests.get("https://ipinfo.io/" + ip + "?token=" + token)
            resJson = json.loads(res.content)

            for host in SAVEHOST:
                if host in resJson["org"]:
                    isLegit = True


            if (isLegit == False):
                print(Back.RED + json.dumps(resJson, indent=2))
            else:
                print(Fore.GREEN + json.dumps(resJson, indent=2))

            time.sleep(2)
        

# Warte auf das Beenden des Prozesses
process.wait()

# Überprüfe den Rückgabewert des Prozesses
if process.returncode == 0:
    print("Befehl erfolgreich ausgeführt")
else:
    print("Fehler beim Ausführen des Befehls")
