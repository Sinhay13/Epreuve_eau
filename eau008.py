'''
Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.


Exemples d’utilisation :
$> python exo.py “4445353”
true


$> python exo.py 42
true

$> python exo.py “Bonjour 36”
false

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys


#Recuperation DATA +teste d'error:
def input_data():
    l = sys.argv[1:]
    if len(l) < 1:
        print("error")
        sys.exit()
    else:
        nombres = " ".join(l)
        return nombres

# Teste de la chaine de caractére:
def full_number_test(nombres):
  try:
    nombres_int= int(nombres)
    print(True)
  except:
    print(False)
  


# Appel des fonction:
nombres = input_data()
full_number_test(nombres)
