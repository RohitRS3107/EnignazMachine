def igninaz(q):
    Q=[]
    qq=list(q)
    QQ=''
    while len(qq)>2:

        if int(str(qq[0])+str(qq[1])+str(qq[2]))>200:
            Q.append(int(qq[0]+qq[1]))
            qq.remove(qq[0])
            qq.remove(qq[0])

        else:
            Q.append(int(qq[0]+qq[1]+qq[2]))
            qq.remove(qq[0])
            qq.remove(qq[0])
            qq.remove(qq[0])
    if len(qq)!=0:
        for i in qq:
            QQ=QQ+i
        Q.append(QQ)
    return Q

