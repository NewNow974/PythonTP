print("Hello World !")


import random
nbMystere=random.randint(0, 20)
nbEssai=6
compteur=1

name = input('Entrez votre nom > ')
print(nbMystere)
while compteur <= nbEssai:
    print("Essai ",compteur,"/6")
    v2 = input('Entrez un nombre entre 0 et 20 > ')
    if v2.isdigit() == False:
        print("Entier incorrect")
    elif int(v2) == nbMystere:
        print("Bravo vous avez gagne",name)
        compteur=nbEssai
    else:
        if int(v2) > nbMystere:
            print("Le nombre est plus petit")
        if int(v2) < nbMystere:
            print("Le nombre est plus grand")
        compteur+=1



