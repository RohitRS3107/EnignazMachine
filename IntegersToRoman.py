dictRomans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
x=input("Enter Romans: ")
x=list(x)
X=[]
a=int()
for i in x:
    X.append(dictRomans[i])
for i in range(1,len(X)):

    ZZ=X[-i]
    X[-i]=X[i-1]
    X[i-1]=ZZ

print(X)
a=X[0]
for i in range(0,len(X)-1):
    if X[i]<X[i+1] or X[i]==X[i+1]:
        a=a-X[i+1]
    else:
        a=a+X[i+1]

print(a)
