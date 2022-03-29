class hasil :
    def hitung (angka):
        print (' ')
        print ('Panjang : ', angka.bil1)
        print ('Lebar : ', angka.bil2)
        print ('Tinggi  : ', angka.bil3)
        print (' ')
        print ('Volume Balok Adalah :', (angka.bil1*angka.bil2*angka.bil3))
        print (' ')

        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang : '))
        self.bil2 = int(input('Masukan Lebar : '))
        self.bil3 = int(input('Masukan Tinggi : '))
        



coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ('|Mencari Volume Balok |')
    
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
