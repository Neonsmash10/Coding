import random

def parier_montant(solde, nom):
    while True:
        montant = input("Entrez le montant à parier : ")
        if not montant.isdigit():
            print("Entre un nombre valide, stp.")
            continue
        montant = int(montant)
        if montant <= 0:
            print("Tu blagues j'espère ?")
            continue
        if montant > solde:
            print("T'as pas assez d'argent pour ça malheureusement.")
            continue
        break

    tirage = random.randint(1, 2)
    if tirage == 1:
        solde += montant
        print(f"Félicitations, {nom}, tu viens de doubler ta mise ! Ton solde est maintenant {solde}€.")
    else:
        solde -= montant
        print(f"Désolé, {nom}, tu as perdu ta mise. Solde restant : {solde}€.")
    return solde

# --- Partie principale ---
nom = input("Comment t'appelles-tu ? ")
if nom == "pantelis":
    print("Pantelis sérieux tu viens miser ta première paye ??")
elif nom == "florian":
    print("Oh un beau gosse entre dans le casino")
    solde = 1000
elif nom == "Théo":
    print("directeur du casino")
    solde = 10000000
elif nom == "Lyam":
    print("tiens c'est pour toi mon gentlemate.")
    solde = "500"
else:
    solde = 100
print(f"\nBienvenue {nom}! Tu as {solde}€ dans ta poche.")

while True:
    print("\nQue veux-tu faire ?")
    print("1.  Parier")
    print("2.  Sortir du casino")

    choix = input("Choisis 1 ou 2 stp : ")

    if choix == "1":
        print("\nChoisis ton jeu :")
        print("1. Pile ou Face")
        print("2. Blackjack (en construction)")

        sous_choix = input("Tape 1 ou 2 : ")

        if sous_choix == "1":
            solde = parier_montant(solde, nom)
            if solde <= 0:
                print(" T'as plus une thune. Ciao le casino.")
                break
        elif sous_choix == "2":
            print(" Le blackjack est pas encore prêt. Patiente un peu.")
        else:
            print("On a dit 1 ou 2... t’inventes des touches là.")
    elif choix == "2":
        print(f" À bientôt {nom}, tu repars avec {solde}€.")
        break
    else:
        print("C'est 1 ou 2, pas plus, pas moins.")
