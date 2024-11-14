x = ['Pada', 'hari', 'Senin', 
'Saya', 'Belajar', 'Mata', 
'Kuliah', 'Algoritma', 
'Pemrograman', 'di', 
'Kelas', 'TI-A',
'Gedung', 'Teori', 'Jurusan', 'Teknik', 
'Elektro', 'Program', 'Studi', 'D3', 'Teknik', 
'Informatika', 'pada', 'Pukul', '07.00', 'WIB',
'sampai', 'dengan', '14.40', 'WIB']
filter = [word for word in x if len(word) > 5]

print(filter)