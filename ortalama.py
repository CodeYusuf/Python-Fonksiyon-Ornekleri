def ortalamaAl (sayilar):
    toplam = 0
    ortalamasi = 0
    for x in range(len(sayilar)):
        toplam += sayilar [x]
    ortalamasi = toplam / len(sayilar)
    return ortalamasi
# Fonksiyon Çağırma
sayiAdet = int(input('Kaç adet sayının ortalamasını alacaksınız: '))
sayilarim = []
for y in range(0, sayiAdet):
    print(y+1, '. sayıyı giriniz: ')
    sayi = int(input())
    sayilarim.append(sayi)
ortalamaAl(sayilarim)
print(ortalamaAl(sayilarim))