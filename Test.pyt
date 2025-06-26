
def afficher_information_personnes(nom, age, taille=0):
    print()
    print("Voici les informations des personnes :")
    print(f"Nom : {nom}")
    print(f"Âge : {age}")

    if age == 17:
        print ("Vous êtes presque majeur !")
    elif age == 18:
        print("Tout juste majeur félicitations !")
    elif 12 <= age <= 18:
        print("Vous êtes adolescent.")
    elif age < 0:
        print("ERREUR : L'âge ne peut pas être négatif.")
    elif age == 1 or  age == 2:
        print("Vous êtes un bébé.")
    elif age > 60:
        print("vous êtes senior.")
    elif age < 10:
        print("Vous êtes enfant.")
    elif age >= 18:
        print("Cette personne est majeure.")
    else:
        print("Cette personne est mineure.")


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR : Vous devez rentrer un nombre pour l'âge")
    return age_int


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

# nom1 = demander_nom()
# nom2 = demander_nom()

# Demande de l'âge
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# Résultat final
# afficher_information_personnes(nom1, age1)
# afficher_information_personnes(nom2, age2)

NB_PERSONNES = 3

for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_information_personnes(nom, age,)