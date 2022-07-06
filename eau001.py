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
        if len(l1_str[i])<2:
            l1_str[i]=f"0{l1_str[i]}"
            l2_str[i]=f"0{l2_str[i]}"
    return l1_str, l2_str


def combinaisons(l1,l2):
    l=[]
    n=0
    nb=0
    for n in range(len(l1)):
        for i in range(len(l1)):
            nb=f"{l1[n]} {l2[i]}"
            l.append(nb)
    return l

def double(l):
    n=0
    for i in l:
        li=l[n].split(" ")
        A= int(li[0])
        B= int(li[1])
        if A==B:
            del l[n]
        n+=1
    return l




l1, l2 = generator_lists()
l= combinaisons(l1,l2)
l=double(l)
print(l)




# trouver comment suprimer les nombres en doublette ordre croissant