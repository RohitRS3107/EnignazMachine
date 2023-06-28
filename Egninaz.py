

import encode
from z import split
from strtolist import zz
from encode import enigma
def Egninaz(i):
    n=int()
    '''x=input('msg')'''
    a=enigma(i)


    if int(a)%2==0:
        a=int(a)+1

        z=int(a)**2
        n=(z+1)/2
        n=int(n)
        n=str(n)
        return n+'3'
    else:
        z = int(a) ** 2
        n = (z + 1) / 2
        return int(n)

def Egninazi():




    a=''
    L=[]
    inpt=input()
    ZZ=split(inpt)
    for i in ZZ:
        L.append(Egninaz(i))



    for i in L:
        a=a+(str(i)+' ')
    print(a)
Egninazi()