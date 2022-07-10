'''
Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.


Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.
'''

import sys

# Recuperation du numeros d'index et teste d'erreurs
def input_data():
    nb=0
    l = sys.argv[1:]
    if len(l)>1:
      print(-1)
      sys.exit()
    try:
      nb= int(l[0])
    except:
      print(-1)
      sys.exit()
    if nb<0:
      print(-1)
      sys.exit()
    return nb

# suite de fibonacci (J'ai mit par default les deux premiere variables de la liste)
def fibonacci(nb):
    n=1
    n0=0
    nf=0
    l=[0,1]
    while nb>0:
        nf=n0+n
        l.append(nf)
        n0=n
        n=nf
        nb-=1
    return l


# teste de la valeur d'index si bien superieur a 1 + application de la suite avec le numeros d'index >1 + affichage de la derniere
# valeur de la liste. 
def afficher_valeur_index(nb):
    if nb==0:
        print(0)
    elif nb==1:
        print(1)
    else:
        nb= nb-1
        l=fibonacci(nb)
        print (l[-1])

# Appel des fonctions : 
nb= input_data()
afficher_valeur_index(nb)

