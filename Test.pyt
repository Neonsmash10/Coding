"""nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
try:
    age_pro = int(age) + 1
except:
 print("arrêtez d'être un idiot " + nom + " et entrez un nombre pour l'âge.")
else:
   print("Bonjour, tu t'appelles " + nom + " et tu as " + age + " ans.")
   print("L'année prochaine, tu auras " + str(age_pro) + " ans.")
n = 0
while n < 1000000000:
    print(n)
    n += 1
    """

mot_de_passe = "1234"
ask = input("Entrez le mot de passe : ")
if ask == mot_de_passe:
    print("Mot de passe correct !")