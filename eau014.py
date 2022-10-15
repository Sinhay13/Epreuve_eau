'''
Créez un programme qui trie les éléments donnés en argument par ordre ASCII.


Exemples d’utilisation :
$> python exo.py Alfred Momo Gilbert
Alfred Gilbert Momo


$> python exo.py A Z E R T Y
A E R T Y Z

Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

#Recuperation DATA +teste d'error
def input_data (): 
  l_int=0  
  l = sys.argv[1:]
  if len(l)<2:
      print("error")
      sys.exit()
  else:
      return l


def comparaison (l):
    dico=dict()
    N=len(l)
    n=0
    while n<N:
        

        

 



l= input_data()
l2=sorted(l,reverse=False)
print(l2)








