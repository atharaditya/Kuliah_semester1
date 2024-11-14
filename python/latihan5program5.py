# program 5 menentukan tahun kabisat

print('Program menentukan tahun kabisat')
print('Masukan nama anda')
nama = input()
print('Masukan tanggal lahir anda')
tanggal = int(input())
print('Masukan bulan lahir anda')
bulan = int(input())
print('masukan tahun lahir anda')
tahun = int(input()) 
if tahun % 400 == 0:
    print(f'Saudara {nama} anda lahir pada tanggal {tanggal} bulan {bulan} tahun {tahun}, anda lahir di tahun kabisat')
else:
    print(f'Saudara {nama} Anda lahir pada tanggal {tanggal} bulan {bulan} Tahun {tahun},Anda tidak lahir di tahun Kabisat')