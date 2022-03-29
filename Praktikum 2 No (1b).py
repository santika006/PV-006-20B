class hasil :
    def hitung (angka):
        print (' ')
        print ('panjang sisi a mendatar : ', angka.bil1)
        print ('panjang sisi b mendatar : ', angka.bil2)
        print ('Tinggi : ', angka.bil3)
        print ('Luas Bangun Jajargenjang Adalah :', angka.bil1*angka.bil3)
        print ('Keliling Bangun Jajargenjang Adalah :', 2* (angka.bil1+angka.bil2))
        
        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang sisi a mendatar : '))
        self.bil2 = int(input('Masukan Panjang sisi b mendatar : '))
        self.bil3 = int(input('Masukan tinggi : '))


coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ('|Mencari Luas Dan Keliling Jajargenjang |')
    print ('Jajar Genjang Memiliki 4 sisi dan tinggi, dimana tiap 2 sisi yang sejajar memiliki panjang yang sama')
    print ('Jika sisi a mewakili sisi alas jajar genjang yang mendatar dan sisi b mewakili sisi miringnya, maka :')
    
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
