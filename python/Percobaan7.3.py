print('Sebelum melakkukan update')
list1 = ['Teknik Informatika','Teknik Elektro',2001,2022]
print('Nilai list pada index 0 adalah',list1[0])
print('Nilai list pada index 2 adalah',list1[2])
print('-'*70)

print('Setelah melakukan update')
list1[2] = 2009
list1[0] = 'Teknologi informasi'
print('Nilai baru pada index 0 sekarang adalah',list1[0])
print('Nilai baru pada index 2 sekarang adalah',list1[2])
print('-'*70)

list1[0:2] = 'D4','Rekayasa Perangkat Lunak'

print('Nilai semua pada list1 setelah di update',list1)