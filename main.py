
#degiskenler
baslik='Haberiniz Olsun'
vade=12 #integer
faizOrani1=1.47 # float
faizOrani2=1.44
faizOrani=1.47

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi="Miraç"
musteriSoyadi="Kuru"
sonucMesaj= mesaj +" "+ musteriAdi+ " "+ musteriSoyadi +"!"

print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1+sayi2)
print(sonucMesaj)

#degiskenler end

#sartBloklari Start
dolarDun= 7.65
dolarBugun=7.65

if dolarDun>dolarBugun:
    print("Azalış oku")
    print("Bitti")
elif dolarDun<dolarBugun:
    print("Artış Oku")
else:
    print("Eşittir Oku")

print("Bitti")

#sartBloklariend

#listeler start
krediler = [Hızlı Kredi", "Maaşını Halkbanktan alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler)) #length

krediler[0] = "Çabuk Krediler"
print(krediler)
print(krediler[3])

#listeler end

#döngüler start 

krediler= ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"]
#alias
for kredi in krediler:
    print("<option>"+kredi+"<option>")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10):
    print(i)

for i in range(0,11,2):
    print(i)

#döngüler end#


#fonksiyonlar start
def kredileriListele():
    krediler=["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
        print("<option>"+kredi+"<option>")

kredileriListele()
kredileriListele():
kredileriListele():
kredileriListele():
kredileriListele():
kredileriListele():
kredileriListele():

#fonksiyonlar end



