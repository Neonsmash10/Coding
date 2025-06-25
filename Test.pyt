
name = input("Enter your name: ")
age = input ("Enter your age: ")

while name == "":
    print("ERROR: Please enter a valid name.")
    name = input("Enter your name: ")

age_prochain = 0
while age_prochain == 0:
    age = input("Enter your age: ")
    try:
        age_prochain = int(age) + 1
    except:
        print("ERROR: Please enter a valid number for age.")

print("Hello " + name + ", You're " + str(age) + " years old.")
print("Next year, you will be " + str(age_prochain) + " years old.")
print("Have a great day!")
