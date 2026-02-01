import subprocess

def ping_check():
    IP = input("Target IP")
    commande = ["ping","-c",'1',IP]
    resultat = subprocess.run(commande,capture_output=True)
    if (resultat.returncode):
        print("not found")

    else:
        (print(" found "))

if __name__ == "__main__":
    ping_check()