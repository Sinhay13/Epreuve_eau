'''
Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.


Exemples d’utilisation :
$> python exo.py “bonjour mathilde, comment vas-tu ?!”
Bonjour Mathilde, Comment Vas-tu ?!


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

#Recuperation DATA +teste d'error
def input_data (): 
  l = sys.argv[1:]
  phrase=" ".join(l) 
  try:
      l_int=int(l[0])
      print("error")
      sys.exit()
  except:
      return phrase

def Majuscule(phrase):
  l=phrase.split()
  l_final=[]
  for word in l:
    word= word[0].upper() + word[1:]
    l_final.append(word)
  phrase=" ".join(l_final)
  print(phrase)
  
  



phrase=input_data()
Majuscule(phrase)

