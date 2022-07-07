#fonction pour ajouter des 0 sur une variable str
def ajout_zero (x):
    if len(x) <2:
        x=f"0{x}"
    return x


# fonction pour transformé chaque nombre de la list en int 
def int_str(nb):
    li=nb.split(" ")
    A= int(li[0])
    B= int(li[1])
    return A ,B




#fonction pour generer deux listes de deux chiffre de 0 à 99 en str
def generator_lists():
    l1=[]
    l2=[]
    l1_str=[]
    l2_str=[]
    for i in range (0,100):
        l1.append(i)
        l2.append(i)
    for i in range(len(l1)):
        l1_str.append(str(l1[i]))
        l2_str.append(str(l2[i]))
    for i in range(len(l1_str)):
        l1_str[i]=ajout_zero(l1_str[i])
        l2_str[i]=ajout_zero(l2_str[i])
    return l1_str, l2_str

#fonction pour faire des deux une liste une seul liste en prenant en compte la totalité des combinaisons avec repetition 
def combinaisons(l1,l2):
    l=[]
    n=0
    nb=0
    for n in range(len(l1)):
        for i in range(len(l1)):
            nb=f"{l1[n]} {l2[i]}"
            l.append(nb)
    return l

# fonction pour trier chaque element de la la liste en ordre croissant
def tri(l):
    n=0
    for i in l:
        A,B=int_str(l[n])
        A_str= str(A)
        B_str=str(B)
        A_str=ajout_zero(A_str)
        B_str=ajout_zero(B_str)
        if B < A:
            l[n]= f"{B_str} {A_str}"
        n+=1
    return l

# fonction pour créer une nouvelle liste sans les variables identique 
def same(l):
    l_final=[]
    for i in range(len(l)):
        if l[i] not in l_final:
            l_final.append(l[i])
    return l_final


# fonction pour suprimer les valeurs quand les deux nombre sont identique
def double(l):
    n=0
    for i in l:
        A,B=int_str(l[n])
        if A==B:
            del l[n]
        n+=1
    return l




# Appel des fonctions : 

l1, l2 = generator_lists()
l= combinaisons(l1,l2)
l=tri(l)
l=double(l)
l_final= same(l)
print(l_final)




