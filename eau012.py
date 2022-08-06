'''
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_bubble_sort(array) {
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

# tri a bulle:
def tri_bulle(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    print(l)


#appels des fonctions:
l=input_data()
l=error(l)
tri_bulle(l)


