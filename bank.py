import random

def parier_montant(solde, nom):
    while True:
        montant = input("Entrez le montant à parier : ")
        if not montant.isdigit():
            print("Entre un nombre valide, stp.")
            continue
        montant = int(montant)
        if montant <= 0:
            print("Tu blagues j'espère ?.")
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

nom = input("Comment t'appelles-tu ? ")
solde = 100
print(f"Bienvenue {nom}! Tu as {solde}€ dans ta poche.")

while True:
    print("\nQue veux-tu faire ?")
    print("1: Parier !!!")
    print("2: Sortir du casino")

    choix = input("Choisis 1 ou 2 stp : ")

    if choix == "1":
        solde = parier_montant(solde, nom)
        if solde <= 0:
            print("Désolé frérot, t'as plus une thune, c’est fini pour toi.")
            break
    elif choix == "2":
        print("Allez, dehors ! Faut être joueur dans la vie, mais pas trop non plus.")
        break
    else:
        print("Écris 1 ou 2, c'est pas si compliqué que ça hein.")
