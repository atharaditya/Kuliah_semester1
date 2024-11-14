import os
os.system('cls')

total = []

awal = int(input('awal range : '))
akhir = int(input('akhir angka sebelum : '))

for i in range(awal, akhir):
    total.append(i * i)

print(total)