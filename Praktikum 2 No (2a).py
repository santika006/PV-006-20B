class hasil :
    def hitung (angka):
        print (' ')
        print ('panjang alas  segitiga/sisi a : ', angka.bil1)
        print ('panjang sisi miring b : ', angka.bil2)
        print ('panjang sisi miring c : ', angka.bil3)
        print ('tinggi segitiga :', angka.bil4)
        print (' ')
        print ('Luas Bangun Segitiga Adalah :', (angka.bil1*angka.bil4)*1/2)
        print ('Keliling Bangun Segitiga Adalah :', angka.bil1+angka.bil2+angka.bil3)
        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang alas segitiga/sisi a : '))
        self.bil2 = int(input('Masukan Panjang sisi miring b : '))
        self.bil3 = int(input('Masukan Panjang sisi miring c  : '))
        self.bil4 = int(input('Masukan tinggi segitiga : '))


coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ('|Mencari Luas Dan Keliling Segitiga |')
    
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

