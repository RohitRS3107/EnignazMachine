dictRomans = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
x=int(input("Enter Romans"))
reminder = x
romansIn = []
romansInn=[]
a=''
for integers,romans in dictRomans.items():
    quotient =reminder//integers
    reminder = reminder%integers

    if reminder>((.79)*integers) and quotient==0:
        romansIn.append(dictRomans[integers])
        romansIn.append(dictRomans[integers/100])
        reminder=reminder%integers
    elif quotient!=4:
        for i in range(0,quotient):
            romansIn.append(romans)




for i in romansIn:
    a=a+i
print(a)


