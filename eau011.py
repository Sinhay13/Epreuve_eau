'''
Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.


Exemples d’utilisation :
$> python exo.py 5 1 19 21
2


$> python exo.py 20 5 1 19 21
1

$> python exo.py -8 -6 4
2

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys


#Recuperation DATA :
def input_data():
    l = sys.argv[1:]
    return l

# Test d'erreur:
def error (l):
    if len(l) <= 1:
        print("error")
        sys.exit()
    l_tested=[]
    for i in range(len(l)):
        try:
            l_tested.append(int(l[i])) 
        except:
            print("error")
            sys.exit()
    return l_tested

# mis en valeur absolu:
def absolu (l):
    for i in range(len(l)):
        if l[i]<0:
            l[i]=-1*l[i]
    return l


# determination de l'ecart minimal:
def minimal_diff (l):
    index= len(l)-1
    minimal= l[0]+l[1]
    while index >= 0:
        for i in range(len(l)):
            diff= l[index]-l[i]
            if diff <0:
                diff=-1*diff
            if minimal > diff and diff!=0:
                minimal= diff
        index -=1
    print(minimal)



# Appel des fonctions : 
l=input_data()
l= error(l)
l= absolu(l)
minimal_diff(l)

