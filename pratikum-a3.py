nama = 'muhammad syawal'
nim = '231031020'
meet = 'pratikum 3'
prodi = 'sistem informasi A'
ttl = '25-11-2005'
alamat = 'Jl.Syamsul Alam Bulu'
asal = 'Parepare'
hobi = 'olahraga'
tinggi = '170'
email = 'syawalm135@gmail.com'

print('-------------------------------------------')
sp = 40
# centered_nama = nama.center(sp).upper()
# print(centered_nama)
print(f"{nama.center(sp).upper()}")
#centered_nim = nim.center(sp)
#print(centered_nim)
print(f'{nim.center(sp)}')
print('\n'*2)
print(f'{meet.capitalize().rjust(sp)}')
print(f'{prodi.title().rjust(sp)}')
print(f'{email.rjust(sp)}')
print('-'*sp)

print(f'''Halo,nama saya {nama.title()} dengan NIM {nim}
dari prodi {prodi.title()},ini adalah file 
{meet.capitalize()},Terima kasih\n''')

print(f'''Biodata saya,
Nama\t:{nama.title()}
NIM\t:{nim}
Prodi\t:{prodi.title()}
TTL\t:{ttl}
Alamat\t:{alamat}
Asal\t:{asal}
Hobi\t:{hobi}
Tinggi\t:{tinggi}cm
''')

stat = 'sir issac newton'
up = stat.upper()
print(up)
up = up.split()
print(up)
print(up[2][0],up[0],up[1])
print('N SIR ISSAC')

print(up[2],up[0][0],up[1][0])
print('NEWTON S I')

print()
stat2 = '&sir$ @issac# *newton.'
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print(up2[0][1:-1],up2[1][1:-1],up[2][0:6])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print(up2)

print("SIR ISSAC NEWTON")