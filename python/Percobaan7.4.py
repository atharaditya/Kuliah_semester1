list1 = ['Teknik Informatika','Teknik Elektro',2009,2022]
list2 = [3,20,22,16,150]
list3 = ['C','B','Sangat Baik','Ungul']
print('Nilai list sebelum di tambah')
print('list1 >>',list1)
print('list2 >>',list2)
print('list3 >>',list3)

print('Nilai list setelah ditambah di awal dngan fungsi insert')
list1.insert(0,'Teknologi Informasi')
print(list1)

print('Nilai list setelah ditambah dari mana sajsa dengan fungsi insert')
list2.insert(3,300)
print(list2)

print('Nilai list setelah ditambah di akhir dengan fungsi append')
list3.append('A')
print(list3)