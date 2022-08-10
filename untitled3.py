i = 2
sayı = int(input("Sayıyı giriniz: "))
liste=[]
çarpan=[]

while i < sayı:

    if sayı % i == 0:
        print(i)
        liste.append(i)
    i += 1
del i
print(liste)
for i in liste:
    bitir=True
    for a in liste:
        if (bitir):
            if(i==a):
                çarpan.append(i)
            elif(i%a==0):
                bitir=False
       
print("\n",*çarpan)