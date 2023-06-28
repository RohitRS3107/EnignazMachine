

import alphas
from alphas import alph
def enigma(a):
    Z = ''
    zz=[]
    for i in a:
        Z = Z + str(alph[i])
        zz.append(alph[i])
    return Z
    print(Z)
    return zz