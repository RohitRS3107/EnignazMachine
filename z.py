def split(x):
    zz=list(x)
    z=[]
    i=''
    while len(zz)>5:

        z.append(zz[0]+zz[1]+zz[2]+zz[3]+zz[4])
        for j in range(0,5):
            zz.remove(zz[0])

    if len(zz)!=0:
        for a in zz:
            i=i+a
        z.append(i)
    return (z)



