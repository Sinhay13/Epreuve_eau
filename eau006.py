'''
Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

#Recuperation DATA +teste d'error
def input_data (): 
  l_int=0  
  l = sys.argv[1:]
  phrase=" ".join(l) 
  try:
      l_int=int(l[0])
      print("error")
      sys.exit()
  except:
      return phrase

def Majuscule(phrase):
  phrase_list=phrase.split()  
  for word in phrase_list:
    lst=list(word)
    N=1
    while N < len(word):
        lst[N]=word[N].upper()
        N+=2
    phrase= ' '.join(lst) 
    print(phrase)





phrase=input_data()
Majuscule(phrase)

# trouver une autre facon de transformer en majuscul

