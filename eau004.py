'''
Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.
'''


import sys

#Récuperation du nombre avec test d'erreurs : 
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

#Teste pour voir si c'est un nombre premier:
def test_premier(nbf):
  if nbf <2:
    return False
  elif nbf > 2:
    for i in range(2, nbf):
      if (nbf % i) == 0:
        return False
  else:
      return True
    
# test pour generer le prochain nombre premier:
def generer_premier(nb):
  while test_premier(nb)==False:
    nb+=1
  print(nb)

#Appel des foctions : 
nb= input_data()
generer_premier(nb)

