# Vize, final puanlarını ve yüzdelik oranlarını parametre olarak alan ve bu puanlar ile yüzdelik oranları çarparak toplayan 
#ve sonucu döndüren bir fonksiyon tanımlayınız.(50, 60, 30, 70)
print((50 + 80)/2)
print((50*0.3)+(80*0.7))
def puanHesap(vize, final, vizeY, finalY):
    return((vize*vizeY)/100 + (final * finalY)/100)
#Fonksiyon Çağırma
print(puanHesap(50, 60, 30, 70))
