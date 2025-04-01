#Demander une adresse ip à l'utilisateur
import platform
#On demande à l'utilisateur de nous fournir l'ip
ip = input("entrez une adresse ip à ping : ")
#On détecte l'os pour adapter la commande
param = "-n" if platform.system().lower() == "windows" else "-c"
#Construction du ping dans un list
commande = ["ping", param, "1", ip]

print("Ping en cours")

#On exécute le ping
try:
    result = subprocess.run(commande, stdout=subprocess.PIPE)
    if result.returncode == 0:
        print("La cible est en ligne")
    else:
        print("Aucune réponse")
except Exception as e:
    print(f"Erreur lors du ping {e}")