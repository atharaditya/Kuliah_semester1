#menggunakan fungsi union() untuk menggabungkan dua set
mahasiswa = set(['Andika','Jaya','Nanda','Andyka','Fajar','Pratama','Diana','Dwi','Apita'])
mhs = set(['Nanda','Ikhwanul','Nadrilin','Fajar','Ulfah','Dwi','Nazarina'])
print('Kelompok 1 = \n',mahasiswa)
print('Kelompok 2 = \n',mhs)
print('\n')

#menggunakan fungsi union() dengan simbol |
print('>>> cara 1 fungsi union dengan simbol pipe | <<<<<')
print(mahasiswa | mhs)
print('\n')

#menggunakan fungsi union cara 2 dengan fungsi set.union
print('>>>> cara 2 fungsi union dengan set.union <<<<<')
print(mahasiswa.union(mhs))