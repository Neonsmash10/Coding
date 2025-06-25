nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
try:
    age_pro = int(age) + 1
except:
 print("Veuillez entrer un âge valide.")
else:
   print("Bonjour, tu t'appelles " + nom + " et tu as " + age + " ans.")
   print("L'année prochaine, tu auras " + str(age_pro) + " ans.")