'''
Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


Exemples d’utilisation :
$> python exo.py bonjour jour
true


$> python exo.py bonjour joure
false


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

#Recuperation DATA +teste d'error
def input_data (): 
    l = sys.argv[1:]
    if len(l)!=2:
      print("error")
      sys.exit()
    try:
        l_int=int(l[0])
        print("error")
        sys.exit()
    except:
        return l
      
#Boucle pour detecter si la chaine de caractére rechercher est presante
def reseach(l):
  response=False
  word= l[0]
  piece= l[1]
  for i in range(len(word)):
    if word[i]==piece[0]:
      if word[i:(len(piece)+i)]==piece:
        response=True
  print(response)
    
#appel des fonctions:
l= input_data()
reseach(l)
