def faktoriyelAl (sayi):
    sonuc = 1
    if (sayi == 0 or sayi == 1) :
        print('Sonuç: ', 1)
    elif (sayi > 1) :
        for x in range (1, sayi+1,1):
            sonuc *= x 
        print('Sonuç: ', sonuc )
    else:
        print('0 veya daha büyük sayısal bir değer girmelisin...')
# Fonksiyonu Çağırma
faktoriyelAl(-1)