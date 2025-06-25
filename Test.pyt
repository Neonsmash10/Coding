nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
try:
    age_pro = int(age) + 1
except:
 print("Veuillez arréter d'être un idiot " + nom + " et entrez un nombre valide pour l'âge.")
else:
   print("Bonjour, tu t'appelles " + nom + " et tu as " + age + " ans.")
   print("L'année prochaine, tu auras " + str(age_pro) + " ans.")