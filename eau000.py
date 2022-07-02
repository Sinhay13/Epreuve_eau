# generateur de la liste : complete et ajout du format trois chifres 
def generator():
    list_nb=[]
    list_str=[]
    for i in range(000,1000):
        list_nb.append(i)
    for i in range(len(list_nb)):
        list_str.append(str(list_nb[i]))
    for i in range(len(list_str)):
        if len(list_str[i])<2:
            list_str[i]=f"00{list_str[i]}"
        if len(list_str[i])<3:
            list_str[i]=f"0{list_str[i]}"
    return list_str

#Determination du chifre mini d'un nombre
def minis(x):
    mini=int(x[0])
    for i in range(len(x)):
        if int(x[i])<mini:
            mini=int(x[i])
    return str(mini)
    
#determination  du chifre maxi d'un nombre
def maxis(x):
    maxi=int(x[0])
    for i in range(len(x)):
        if int(x[i])>maxi:
            maxi=int(x[i])
    return str(maxi)

#Determination du deuxieme chifre le plus petit sur un nobre à trois chiffres
def mediums (x,mini,maxi):
    medium= x[0]
    for i in range(len(x)):
        if x[i] != mini:
            if x[i] != maxi:
                medium = x[i]
    return medium

#trie d'un nombre a trois chiffres avec appel des methodes mini max et medium
def tri(nb):
    nb_list=[1,2,3]
    nb_list[0]=nb[0]
    nb_list[1]=nb[1]
    nb_list[2]=nb[2]
    mini=minis(nb_list)
    maxi=maxis(nb_list)
    medium=mediums(nb_list,mini,maxi)
    nb=f"{mini}{medium}{maxi}"
    return nb

 #Comparaison des nombres la liste apres appel methode tri et creation d'une listes sans doublete        
def not_same (list_nb):
    list_nb2=[]
    for i in range(len(list_nb)):
        nb = tri(list_nb[i])
        if nb not in list_nb2:
            list_nb2.append(nb)
    return list_nb2

#supression nombres dont les chiffre aparaissent plusieur et creation + affichage de la liste final
def final(list_nb2):
    list_final=[]
    for i in list_nb2:
        A=i[0]
        B=i[1]
        C=i[2]
        if not A==B:
            if not B==C:
                if not A==C:
                    list_final.append(i)
    print(list_final)




# appel des diferentes fonctions :
list_nb= generator()
list_nb2=not_same(list_nb)
final(list_nb2)
