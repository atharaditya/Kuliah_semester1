import os
os.system('cls')

kata_1 = 'Aku Ganteng Banget'
kata_2 = 'Emang Bener ! '
kata_3 = 'Saya Sudah Bisa Membuat Fungsi dengan python'

print('original : ')
print(kata_1)
print(kata_2)
print(kata_3)

kebalikan_1 = ' '.join(reversed(kata_1.split()))
kebalikan_2 = ' '.join(reversed(kata_2.split()))
kebalikan_3 = ' '.join(reversed(kata_3.split()))

print('\nkebalikan : ')
print(kebalikan_1)
print(kebalikan_2)
print(kebalikan_3)