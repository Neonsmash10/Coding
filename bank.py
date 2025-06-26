nom = input("Comment t'appelles tu ?")
solde = 100
print(f"Bienvenue {nom}! Vous avez ${solde} dans votre compte bancaire.")
print("Que voulez-vous faire avec cet argent ?")
gambling = input("1. Pourquoi garder cet argent quand on peut le parier ?")
print("En construction...")

def parier_montant(solde):
    print("Combien voulez-vous parier ?")
    montant = input("Entrez le montant à parier : ")
    import random
    tirage = random.randint(1, 2)
    if tirage == 1:
        print(f"Félicitations, {nom}, vous venez de le double de votre mise !")
        solde += montant
    else:
        print(f"Désolé,{nom}, vous avez perdu l'entièreté de votre mise.")
        solde -= montant
    return solde
