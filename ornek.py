def agacciz (yukseklik, karakter = '*'):
    b = yukseklik
    for x in range (1, yukseklik+1):
        print(b*' ', (2*x-1)*karakter)
        b -= 1
# Fonksiyonu Çağırma
agacciz(10)