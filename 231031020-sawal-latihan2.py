while True:
    try:
        inp = str(input('Masukkan suatu input: '))
        if len(inp) != 3:
            print('Panjang string', len(inp), 'tidak sama dengan 3')
        else:
            print('Panjang input sesuai yang diinginkan')

        ulangi = input('apakah kau mau mengulangi anjing ya/tidak :')
        if ulangi != 'ya':
            break
    except ValueError:
        print('kontol')
    

