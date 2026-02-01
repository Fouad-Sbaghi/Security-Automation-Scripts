import subprocess

def scan():
    ip = input("Target TP")
    command = ["nmap", "-sV", "-T4", ip]
    resultat = subprocess.run(command,capture_output=True,text=True)
    print(resultat.stdout)

    with open("rapport_scan.txt", "w") as f:
        f.write (f"rapport de scan pour {ip}\n")
        f.write(resultat.stdout)
    
    print("Scan terminé et le résultat est dans rapport_scan.txt")

if __name__ == "__main__":
    scan()