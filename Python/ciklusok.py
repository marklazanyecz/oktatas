# Mikor while, mikor for
# Feladat többszöri végrehajtása vs adott számú ismétlés vagy bejárás/iterálás

# Ciklusfutás mahinálása:
# break == megszakítja a ciklus teljes futását
# continue == a következő iterációra léptet. 
# Continue esetében a kulcsszó alatt, de még az iterációban lévő parancsok nem futnak le

while True:
    break

while not False:
    break

i = 1
while i > 1:
    break

j = 12
while i > 0 and j > 10:   # A feltételrendszer ugyan olyan mint az elágazásoknál
    break




while True:            # Ciklusban a ciklus != rekurzió
    while not False:
        break
    break




i = 10
while i > 0:
    i -= 1
else:
    print(" i nempozitív")




while True:   # Ha break-el ér véget a ciklus, akkor az else ág nem fut le
    break     # Ha el se kezdődik, vagy végigmegy akkor lefut
else:
    print("nem fut le")




szam = 0
while szam < 50:
    if szam % 2 == 1:
        szam += 1
        continue
    else:
        print(szam)
        szam += 1




for i in range(10):
    print(i)

for i in range(3,10):
    print(i)

for i in range(3,10,2):  # 3=start, 10=stop, 2=step
    print(i)             # start alapértelmezetten 0, a step pedig 1

x = 10
y = 25
z = 4
for i in range(x,y,z):
    print(i)




for i in "alma":
    print(i)

szoveg = "szolocukor"
for i in szoveg:
    print(i)

for i in range(len(szoveg)):
    print(i)




for i in range(1,11):
    for j in range(1,11):
        print(i*j, " ", end="")
    print()




for i in range(50):
    if i % 2 == 1:
        continue
    else:
        print(i)