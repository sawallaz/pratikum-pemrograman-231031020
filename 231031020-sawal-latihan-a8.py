passwords = ["123", "456", "789"]
max_attempts = 3
correct_passwords = 0
locked_account = False

while correct_passwords < len(passwords) and not locked_account:
    attempts = 0

    while attempts < max_attempts:
        password = input(f"Masukkan password {correct_passwords + 1}: ")
        attempts += 1

        if password == passwords[correct_passwords]:
            print(f"Password {correct_passwords + 1} benar!")
            correct_passwords += 1
            break
        else:
            if attempts == max_attempts:
                print("Anda telah melebihi batas percobaan untuk password ini. Akun terkunci.")
                locked_account = True
                break
            else:
                remaining_attempts = max_attempts - attempts
                print(f"Password salah. Anda memiliki {remaining_attempts} percobaan lagi untuk password {correct_passwords + 1}.")

if correct_passwords == len(passwords) and not locked_account:
    print("Selamat Anda Login!")