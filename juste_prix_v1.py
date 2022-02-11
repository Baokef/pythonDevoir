from random import randint


print("bienvenu dans le juste prix !")
propostionDePrix = int(input("Veuillez entrer votre prix : "))

justPrix = randint(1, 100)
while True:
    if propostionDePrix < justPrix:
        print("c'est moins ! \n")
        propostionDePrix = int(input("Veuillez entrer votre prix : "))

    elif propostionDePrix > justPrix:
        print("c'est plus ! \n")
        propostionDePrix = int(input("Veuillez entrer votre prix : "))

    elif propostionDePrix == justPrix:
        print("Félicitations...! \n")
        print(justPrix)

        break
    else:
        exit()
