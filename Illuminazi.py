from codes import codes
from enginazing import igninaz

from strtolist import zz
from z import split

def Illuminaz():
    zzz=[]
    i=str(input())
    x=str(i)
    zzzz=x.split(' ')
    ZZZ=''




    for x in zzzz:
        if x[-1]=='3':
            x=str(x)
            x = list(x)
            x.pop(-1)
            ww = ''
            for i in x:
                ww = ww + i
            a = ww
            a=int(a)

            z=int(a**2)

            Z=int(a)-1
            ZZ=Z**2
            A=z-ZZ
            q=(A**(1/2))
            q=int(q)
            q=q-1
            q=str(q)
            '''print(q)'''
            q=igninaz(q)

            for i in q:

                zzz.append(codes[int(i)])


        else:
            x=int(x)
            z = int(x ** 2)

            Z = int(x) - 1
            ZZ = Z ** 2
            A = z - ZZ
            q = (A ** (1 / 2))
            q = int(q)
            q = str(q)
            q = igninaz(q)

            for i in q:

                zzz.append(codes[int(i)])


    for i in zzz:
        ZZZ=ZZZ+str(i)
    print(ZZZ)


'''inpt=input()
ZZ=split(inpt)
print(ZZ)
for i in ZZ:
    Illuminaz(int(i))'''
Illuminaz()