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

# Comparaison de deux élément par ordre ascii:
def compare (a,b):
    n=0
    if a==b:
        return 0
    while a[n]==b[n]:
        n+=1
    return ord(a[n])-ord(b[n])

# Mis en ordre ascii avec tri à bulle: 
def bulle_ascii (l):
    n=0
    limite=len(l)
    while n<limite:
        if n+1==limite:
            return l
        tmp=compare(l[n],l[n+1])
        if tmp >0:
            l_tmp= l[n]
            l[n]=l[n+1]
            l[n+1]=l_tmp
            n=0
        else:
            n+=1



#Transformation de la la liste en chaine de caractére:
def final(l):
    phrase=" ".join(l)
    print(phrase)

        



# Appel des fonctions: 
l=input_data()
l=bulle_ascii(l)
final(l)







        