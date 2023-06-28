dictRomans = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
x=int(input("Enter Romans"))
reminder = x
romansIn = []
a=''
for integers,romans in dictRomans.items():
    quotient =reminder//integers
    reminder = reminder%integers
    for i in range(0,quotient):

        romansIn.append(romans)
x=str(x)

for i in romansIn:
    a=a+i
print(a)


