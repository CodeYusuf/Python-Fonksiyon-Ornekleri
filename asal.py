def asal (sayi) :
    adet = 0
    for x in range(2, sayi+1):
        if sayi % x == 0 :
            adet+=1
    if adet == 1 :
        print('Asaldır...')
    else:
        print('Asal değildir...')        

# Fonksiyon çağırma
asal(6)