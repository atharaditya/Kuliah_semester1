#menggunakan fungsi difference() untuk menggabungkan dua set
mahasiswa = set(['Andika','Jaya','Nanda','Andyka','Fajar','Pratama','Diana','Dwi','Apita'])
mhs = set(['Nanda','Ikhwanul','Nadrilin','Fajar','Ulfah','Dwi','Nazarina'])
print('Kelompok 1 = \n',mahasiswa)
print('Kelompok 2 = \n',mhs)
print('\n')

#menggunakan fungsi difference() dengan simbol -
print('>>>>> cara 1 fungsi difference() dengan simbol -')
print(mahasiswa-mhs)
print('\n')

#menggunakan fungsi difference() dengan fungsi set.difference()
print('>>>>> cara 2 fungsi difference() dengan fungsi set.difference()')
print(mahasiswa.difference(mhs))