
class hasil :
    def hitung (angka):
        print (' ')
        print ('Panjang sisi : ', angka.bil)
        print (' ')
        print ('Luas Bangun Persegi Adalah :', angka.bil**2)
        print ('Keliling Bangun Persegi Adalah :', 4*angka.bil)
        print (' ')

        
class nilai(hasil) :
    def __init__(self):
        self.bil = int(input('Masukan Panjang sisi : '))



coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ('|Mencari Luas Dan Keliling Persegi |')
    
    objek = nilai()
    objek.hitung()
    print(' ')
    coba = input('Mau Menghitung Lagi : ')
    if coba == ('y') or coba == ('Y') :
        print (' ')
        continue
    elif coba == ('n') or coba == ('N') :
        print ('Terima Kasih')
        break
    else :
        print ('Pilihan yang Anda Masukan Salah')
        break
