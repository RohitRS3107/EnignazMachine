import codes
from codes import codes
from enginazing import igninaz

def illuminate(zz):
    z=[]
    z=igninaz(zz)
    ZZ=[]
    A=''
    for i in z:
        A = A + str(codes[i])
        ZZ.append(A)

    return ZZ[-1]
