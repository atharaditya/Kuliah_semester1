import os
os.system('cls')

string = 'Budi dan Roni sedang kerja kelompok di rumah Asep'
print('string original : ',string)

upper_count = sum(1 for element in string if element.isupper())
lower_count = sum(1 for element in string if element.islower())

print('jumlah karakter uppercse pada string : ', upper_count)
print('jumlah karakter lowercase pada string : ',lower_count)