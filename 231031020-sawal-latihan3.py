nama = input("Nama karyawan: ")
pendapatan = int(input("Pendapatan: "))
print("Nama karyawan:", nama)
print("Pendapatan:", pendapatan)

if pendapatan > 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")
