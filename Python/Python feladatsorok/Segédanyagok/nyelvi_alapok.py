# PYTHON: magas szintű programozási nyelv, interpretált fordítással
# Legelterjedtem fordítás: python -> c nyelvi alapú fordító -> bytekód -> gépi kód


# Előny: emberek számára könnyen olvasható kóddal lehet megvalósítani rengeteg,
# a háttérben alacsony szintű műveletet
# Ennek hatására rengeteg külső könyvtár elérhető, szinte bármit meg lehet valósítani


# Hátrány: A sorról sorra fordítás alapvetően lassabb mint az állományi fordítás,
# viszont egy köztes kódot is generálnia kell a fordítónak a gépi nyelvre fordításhoz
# Ez sokkal lassabb más programozási nyelvekhez képest, különösképpen nagyobb algoritmusoknál
# Ahhoz, hogy bármit megvalósítsunk ismernünk is kell ezeket a külső könyvtárakat,
# adott esetben le is kell őket töltenünk, amelyek tárhelyet foglalnak a lemezen,
# és foglalhatnak a stacken is


# Szintaxis: magas szintű nyelv lévén már-már majdnem formális emberi nyelv,
# Bizonyos kulcsszavak és kifejezések mégis valamivel alacsonyabb szintűek, pl.: __eq__
# Utasítások végét az újsor karakter jelöli
# Kódblokkokat a : karakterrel tudunk nyitni, ez után egyszerűen szóköz vagy tab behúzással
# jelöljük mely utasítások hova tartoznak


# Sorközi komment: # :), mindent ami ez után van figyelmen kívül hagyja a fordító
# Többsoros komment:
"""
Ez például az
de a zöldet jobban szeretem, sajnálom
"""


# Nem kimondott objektum orientált nyelv, viszont minden megvalósítható ezen a téren is
# Dinamikusan típusos nyelv, fordítási időben történik az elemek típusérték adása és felismerése




# FÜGGVÉNYEK
def kiir():  # A függvény kiír valamit
    print()

def visszakuld(valami):   # A függvény paraméterben kapja a valami változót, majd visszaadja
    return valami




# ALAPVETŐ ADATTÍPUSOK
# int, float, str, bool, NoneType
# léteznek különlegesebb típusok is még amelyek mélyebb tudást igényelnek, pl.: complex, bytearray
# Típusok konkrét megadása: típus(elem) pl.: str(7)




# VÁLTOZÓK
# Változónév: lehetőleg leírja amire használva van, ékezetmentes, nem tiltott szó pl.: for, and, stb
# Változó létrehozása:
x = 10




# KONZOL INPUT/OUTPUT
# Kiíratás konzolra:
print("X értéke: " + x)     # print() Egyszerű konzolra kiíratás, csak stringeket ír ki
print(f"X értéke {x}")      # f""     Formázott kiíratás

# Bekérés konzolról
# input() függvénnyel, csak string adattípust olvas be
szoveg = input()   # Alapvetően string lesz

# Kasztolás
szam = int(input())
lebegoPontos = float(input())
igazsagErtek = bool(input())




# Aritmetikai műveletek: + összeadás, - kivonás, * szorzás, / osztás,
# // maradék nélküli osztás, % maradékos osztás, ** hatványozás

# Logikai kiértékelések: not, and, or, ^ (kizáró vagy, xor)
# Operandusok: <, >, ==, !=, <=, >=

x = 15
x = str(x)
y = 12
y = -y  # Integer változó negatívvá tétele, lebegőpontossal is működik
y = abs(y)  # Változó abszolút értéke, mindíg pozitív lesz
igaz = False
igaz = not igaz   # Boolean érték tagadása




# ELÁGAZÁSOK
if x > y:   # Ha x nagyobb mint y akkor belép a kódblokkba
    pass    # Space vagy Tab jelenti a behúzását


if 0 < x and x < 50:  # rövidítés: if 0 < x < 50:
    pass


if x < 0:   # Mivel x nem kisebb mint 0 ezért nem lép be
    pass
elif x == 15:   # Mivel ez igaz, ennek a feltételnek lép be az ágjába
    pass


if x <= y:
    pass
elif x == y:
    pass
else:       # Mivel egyik előző feltétel sem teljesült, így ez az ág fut le
    pass    # Ez a részlet csak akkor fut le ha egyik előző feltétel sem teljesült, viszont ez nem garantált!


if x > 15:
    pass
elif x <= 6:
    pass
elif y != 45:
    pass
elif x+y == 142:
    pass
else:
    print(x)    # Csak akkor fut le ha egyik előző feltétel sem teljesült

print(x)    # Mindenképp lefut




# Logikai értékeket lehet csatolni a feltételbe

if ((x+y**y/x-23*x) == 10) and (x < 10) or (x == y) and not (x == 10):
    pass

# Hosszabb, bonyolultabb feltételrendszernél érdemes zárójeleket használni
# Pythonban nem kötelező, de mégis megengedett