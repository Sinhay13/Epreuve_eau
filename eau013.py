'''
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_select_sort(array) {
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6


$> python exo.py test test test
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


Wikipedia vous présentera une belle description de cet algorithme de tri.
'''

import sys


#Recuperation DATA :
def input_data():
    l = sys.argv[1:]
    return l


# Test d'erreur:
def error(l):
    if len(l) <= 1:
        print("error")
        sys.exit()
    l_tested = []
    for i in range(len(l)):
        try:
            l_tested.append(int(l[i]))
        except:
            print("error")
            sys.exit()
    return l_tested


# Tri par selaction:
def tri_selection(l):
    for i in range(len(l)):
        min = i
        for j in range(i + 1, len(l)):
            if l[min] > l[j]:
                min = j
        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp
    print(l)


# Appels des fonctions :
l = input_data()
l = error(l)
tri_selection(l)
