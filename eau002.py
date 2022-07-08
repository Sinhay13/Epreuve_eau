import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)<1:
      print("erreur")
      sys.exit()
    return l

#boucle while pour inverser les arguments 
def inverse_data(l):
  n=len(l)-1
  while n>=0:
    print(l[n])
    n=n-1
    
    
  
  
# appel des fonctions 

l=input_data()
inverse_data(l)
