import os
from rich import *
from tkinter import messagebox

a=input("напишите имя файла для чтения: ")
fil=open(a)

content=fil.readlines()
if len(content)==3:
    nushno=content[1][1:]
    nushno=nushno.replace(" ","")
    nushno=nushno.replace(";"," ")
    g=[nushno.split()]
    g=g[0]
    del g[-1]
    poradok=content[2]
elif len(content)==4:
    messagebox.showinfo(0,content[1])
    nushno=content[2][1:]
    nushno=nushno.replace(" ","")
    nushno=nushno.replace(";"," ")
    g=[nushno.split()]
    g=g[0]
    del g[-1]
    poradok=content[3]
por=list(poradok.split())

n=1

l=[]
por=sorted(por)
g=sorted(g)
bobo=[]
slova=[]

for x in range(len(por)):
    karandash=list(por[x].replace(":"," ").split())
    slova.append([int(karandash[0]),karandash[1],int(karandash[2])])
for x in range(len(g)):
    sasas=list(str(g[x]).replace(':',' ').split())
    prop=sasas[0]
    bobo.append(prop)


slova=sorted(slova)
met=1
sasa=0
while True:
    if sasa!=1:
        if g[bobo.index(str(met))][2:][0]!='$':
            kra=list(str(g[bobo.index(str(met))][2:]).replace(':',' ').split())
            if len(kra)==1:
                print(kra[0])
            else:
                print(kra[1])
        else:
            os.system('start '+g[met-1][2:][1:])
    otvetik=input()
    for i in range(len(slova)):
        if slova[i][0]==met:
            if slova[i][1]==otvetik:
                met=slova[i][2]
                sasa=0

                break
    else:
        print("такого ответа нет")

        sasa=1
    for sa in range(len(slova)):
        if slova[sa][0]==met:
            break
    else:
        break
if g[bobo.index(str(met))][2:][0]!='$':
    kra=list(str(g[bobo.index(str(met))][2:]).replace(':',' ').split())
    if len(kra)==1:
        print(kra[0])
    else:
        print(kra[1])
else:
    os.system('start '+g[met-1][2:][1:])
print("history is ended")
input()
