#membuat tuple car standar
tuple_jenjang_pendidikan = ('Diploma Tiga', 'Diploma Empat')

#memebuat tuple tanpa kurung
tuple_jenis_kelamin = 'laki-laki', 'perempuan'

#membuat tuple mengunakan fungsi tuple()
tuple_status_kelululsan = tuple(['lulus','Tidak Lulus'])

print('1) Tuple cara standar')
print(tuple_jenjang_pendidikan)
print()
print('2) Tuple tanpa tanda kurung')
print(tuple_jenis_kelamin)
print()
print('3) Tuple mengunakan fungsi tuple')
print(tuple_status_kelululsan)

print()
print()

#membuat tuple cara standar
tuple_jenjang_pendidikan = ('Diploma Tiga', 'Diploma Empat')

print(tuple_jenjang_pendidikan[1]) #mencetak tuple indek ke 1
print(tuple_jenjang_pendidikan[0]) #mencetak tuple indek ke 0

print()
print()

#membuat tuple cara standar
tuple_jenjang_pendidikan = ('Diploma Tiga', 'Diploma Empat')


print(tuple_jenjang_pendidikan[-2]) #mencetak tuple indek ke 1
print(tuple_jenjang_pendidikan[-1]) #mencetak tuple indek ke 0

print()
print()

#Contoh slicing tuple
tuple_jurusan = ('mesin','sipil','elektro','akutansi',
                'akutansi','bisnis','pertanian','kelautan')

print(tuple_jurusan[0:1])
print(tuple_jurusan[1:3])
print(tuple_jurusan[0-1])
print(tuple_jurusan[-1:-3])
print(tuple_jurusan[-3:-1])

print()
print()

#Contoh slicing tanpa batas
tuple_jurusan = ('mesin','sipil','elektro','akutansi',
                'akutansi','bisnis','pertanian','kelautan')

print(tuple_jurusan[0])
print(tuple_jurusan[1:])
print(tuple_jurusan[2:])
print(tuple_jurusan[0:])
print(tuple_jurusan[:0])
print(tuple_jurusan[:1])
print(tuple_jurusan[:3])
print(tuple_jurusan[:4])

print()
print()

#mengubah data dalam list
list_jurusan = ['mesin','sipil','elektro','akuntansi',
                'bisnis','pertanian','kelautan']
list_jurusan[4] = 'administrasi bisnis'
print(list_jurusan)

print('~'*20)

#mengubah data dalam tuple
tuple_jurusan = ('mesin','sipil','elektro','akuntansi',
                'bisnis','pertanian','kelautan')
list_jurusan[4] = 'administrasi bisnis'
print(tuple_jurusan)

print()
print()

#membuat tuple data mahasiswa
nama_mhs = ('Awang','Pontianak','18')

#mengekstrak sata atau dinamakan juga
#dengan sequence unpacking
nama, tempatlhr, usia = nama_mhs

#setiap variabel di atas akan memiliki nilai
#dari setiap isi tuple secara berurutan
print('Nama Mahasiswa :',nama)
print('Tempat Lahir   :',tempatlhr)
print('Usia           :',usia)

print()
print()

#menggabungkan dua tuple
no_urut = (1,2,3,4,5)
nilai = (78,76,88,90)

NA = no_urut + nilai
print(NA)

NIM = ('001','002','003')
Nama = ('Diana','Desi','Tekla')

daftar_mhs = NIM + Nama
print(daftar_mhs)

print()
print()

#menggunkan funsi pada tuple
nilai_alpro = (88,89,80,87,90,92,87,75)
print('Nilai algoritma pemrograman : ',nilai_alpro)
print('Nilai tertinggi pemrogramn :',max(nilai_alpro))
print('Nilai terendah algoritma pemrograman :',min(nilai_alpro))