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

# mise sous forme de liste:
def faire_une_liste (phrase):
  liste=list(phrase)
  return liste

#majuscule une sur deux :
def Majuscule(liste):
  for i in range(len(liste)):
    if liste[i] != " " and i%2==0:
      liste[i]= liste[i].upper()
    else:
      liste[i]=liste[i].lower()
  return liste

# Gestion des espaces vides:
def vide (liste): 
  for n in range(len(liste)):
    if liste[n] == " ":
      if liste[n-1].isupper():
        liste[n+1]=liste[n+1].lower()
        liste= liste[0:n+2]+Majuscule(liste[n+2:])
      else:
        liste= liste[0:n+1]+Majuscule(liste[n+1:])
  return liste

  #Affichage resultat
def resultat (liste):
  phrase = "".join(liste)
  print(phrase)



#appel des fonctions: 
phrase=input_data()
liste= faire_une_liste(phrase)
liste=Majuscule(liste)
liste=vide(liste)
resultat(liste)





