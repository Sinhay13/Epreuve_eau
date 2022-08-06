'''
Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24


$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys


#Recuperation DATA +teste d'error:
def input_data():
    l = sys.argv[1:]
    if len(l) != 2:
        print("error")
        sys.exit()
    else:
        try:
            int_1 = int(l[0])
            int_2 = int(l[1])
            return int_1, int_2
        except:
            print("error")
            sys.exit()


# Boucle pour afficher tout les nombres:
def count_number(int_1, int_2):
    l_int = []
    l_str = []
    for i in range(int_1, int_2):
        l_int.append(i)
    for i in l_int:
        l_str.append(str(i))
    output = " ".join(l_str)
    print(output)


# Appel des fonctions:
int_1, int_2 = input_data()
count_number(int_1, int_2)