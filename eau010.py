'''
Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.


Exemples d’utilisation :
$> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
6


$> python exo.py test test test
0

$> python exo.py test boom
-1

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys


#Recuperation DATA :
def input_data():
    l = sys.argv[1:]
    return l

# Recherche de l'index: 
def index_wanted(l):
    word = l[-1]
    i=0
    for words in l :
        if l[i]== word:
            result =i 
        else:
            i+=1
    return result

#Teste d'erreur:
def error_test(l, result):
    index_max= len(l)-1
    if result== index_max:
        result=-1
    print(result)

#Appels des fonctions :
l=input_data()
result=index_wanted(l)
error_test(l, result)


    