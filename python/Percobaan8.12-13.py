#percobaan 8.12
#menggunakan fungsi symmetric_difference() untuk menggabungkan dua set(menjadi satu set)
mahasiswa = set(['Andika','Jaya','Nanda','Andyka','Fajar','Pratama','Diana','Dwi','Apita'])
mhs = set(['Nanda','Ikhwanul','Nadrilin','Fajar','Ulfah','Dwi','Nazarina'])

print('Nama Mahasiswa yang ikut dalam satu grup saja')
print(mahasiswa.symmetric_difference(mhs),'\n')
print()
print()

#percobaan 8.13
mahasiswa = set(['Andika','Jaya','Nanda','Andyka','Fajar','Pratama','Diana','Dwi','Apita'])
mhs = set(['Nanda','Ikhwanul','Nadrilin','Fajar','Ulfah','Dwi','Nazarina'])

print('Nama Mahasiswa yang bukan kelompok mhs')
print(mahasiswa.difference(mhs),'\n')