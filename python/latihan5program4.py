# program 4 mengetahui jenis segitiga

print('program mengetahui jenis segitiga')
print('=================================')
x = input('masukan sisi kiri segitiga = ')
y = input('masukan sisi tepi segitiga = ')
z = input('masukan sisi alas segitiga = ')
if x==y==z :
   print(f'segitiga sama sisi, dimana memiliki sisi x={x}, y={y}, z={z}') 
elif x==y or x==z or y==z :
   print(f'segitiga sama kaki, dimana memiliki nilai sisi x={x}, y={y}, z={z}')
else :
   print(f'segitiga sembarang, dimana memiliki nilai sisi x={x}, y={y}, z={z}')