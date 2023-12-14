def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(30))
    print('BANGUN DATAR PERSEGI'.center(30))
    print('='*60)

def inputan():
    panjang = float(input('Masukan Panjang:'))
    lebar = float(input('Masukan Lebar:'))
    return panjang,lebar

def hitung (panjang,lebar):
    luas = panjang*lebar
    kel = (panjang+lebar)*2
    return luas,kel


def tampil (pesan,nilai):
    print(f'Hasil perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('apakah ingin melanjutkan?(y/n)')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('sampai jumpa')
    return a
a = True
while a:
    # judul
    judul()
    #inputan panjang dan lebar
    panjang,lebar = inputan()
    # hitung luas dan kel
    kel ,luas = hitung(panjang,lebar)
    #cetak atau display
    tampil('luas',luas)
    tampil('keliling',kel)

    a = pilihan()

    print('='*60)

