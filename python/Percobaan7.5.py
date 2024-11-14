list1 = ['Teknik Informatika','Teknik Elektro',2009,2022]
list2 = [3,20,22,16,150]
list3 = ['C','B','Baik','Sangat baik','Unggul']

print('Menghapus nilai list dengan fungsi pop')
list1.pop()
print(list1)

print('Menghapus nilai list dengan fungsi del')
del list2[4]
print(list2)

print('Menghapus nilai list dengan fungsi remove')
list3.remove('C')
print(list3)