#menggunakan fungsi intersection() untuk menggabungkan dua set
mahasiswa = set(['Andika','Jaya','Nanda','Andyka','Fajar','Pratama','Diana','Dwi','Apita'])
mhs = set(['Nanda','Ikhwanul','Nadrilin','Fajar','Ulfah','Dwi','Nazarina'])
print('Kelompok 1 = \n',mahasiswa)
print('Kelompok 2 = \n',mhs)
print('\n')

#menggunakan fungsi intersection() dengan simbol &
print('>>>>> cara 1 fungsi intersection() dengan simbol &')
print(mahasiswa&mhs)
print('\n')

#menggunakan fungsi intersection() dengan fungsi set.intersection()
print('>>>>> cara 2 fungsi intersection() dengan fungsi set.intersection()')
print(mahasiswa.intersection(mhs))