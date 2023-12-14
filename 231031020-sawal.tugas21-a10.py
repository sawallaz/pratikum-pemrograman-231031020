while True:
    try:
        x = int(input('Masukan Angka(0 sebagai penutup!) :'))
        if x == 0:
            print('Makasih Sayang')
            break
        elif x % 2 == 0:
            print (f'{x}Angka Harus Genap!')
        else:
            print(f'{x} Angka Harus Ganjil!')
    except ValueError:
        print('Masukan Angka Yang Benar')