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

# creation d'une liste avec la valeur ascii des lettre ce trouven a n position: 
def liste_ascii (l, n=0):
    l_ascii=[]
    for word in l:
        l_ascii.append(str(ord(word[n])))
    return l_ascii
    

# creation d'un dictionaire avec les deux listes:
def dictionaire(l, l_ascii):
    dico= dict(zip(l_ascii, l))
    cle= sorted(dico)
    return dico, cle

#teste des lettre en double:
def doublette (l, dico, cle, n=0):
    N=len(cle)
    while n<N:
        pass


# creation d'une liste ordoner et affichage du resultat:
def trier(dico, cle):
    l_final=[]
    for i in range(len(cle)):
        l_final.append(dico[cle[i]])
    phrase=" ".join(l_final)
    print(phrase)

      
#appel des fonction:
l= input_data()
l_ascii=liste_ascii(l)
dico,cle= dictionaire(l, l_ascii)
#dico,cle=doublette(dico, cle)
trier(dico, cle)









