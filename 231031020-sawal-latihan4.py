pendapatan = int(input('masukan pendapatan (0-5001):'))
presentase=''


if pendapatan <= 1000:
    presentase += '0'
elif pendapatan <= 2000 and pendapatan >= 1001:
    presentase += '10'
elif pendapatan <= 3000 and pendapatan >= 2001:
    presentase += '20'
elif pendapatan <= 4000 and pendapatan >= 3001:
    presentase += '30'
elif pendapatan <= 5000 and pendapatan >= 4001:
    presentase += '40'
else:
    presentase += '50'

bonus = pendapatan * ((int(presentase)/100)) 
print(f'pendapatan :{pendapatan}')
print(f'presentase :{presentase}%')
print(f'bonus :{bonus}')
print(f'juhmlah total :{pendapatan + bonus}')
