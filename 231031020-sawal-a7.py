chance = 3
pw = 'sawal123'

while True:
    inp = input('Silahkan masukkan password : ')
    if inp != 'sawal123':
        chance -= 1
        print(f'Password salah!')
        print(f'anda punya {chance} kesempatan tersisa ')
        if chance == 0:
            print('anda kehabisan kesempatan!')
            break
    else:
        print('selamat datang!')
        break
