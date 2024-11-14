print('>>>>>>>>>> Nilai awal set mata kuliah')
mata_kuliah = {'pancasila','matematika 1','PTI','Pemrograman Terstruktur'}
print(mata_kuliah)

print('>>>>> menambah set dengan fungsi add()')
mata_kuliah.add('paket program terapan')
print(mata_kuliah) 

mata_kuliah.add('paket program terapan','algoritma pemrograman')
print(mata_kuliah)

print('>>>>> menambah set dengan fungsi update()')
mata_kuliah.update({'algoritma pemrograman','pemrograman web'})
mata_kuliah.update({'praktikum paket program terapan'})
print(mata_kuliah)