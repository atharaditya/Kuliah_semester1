list_angka =[1,2,3,4,5,6,7,8,9]
ganjil = 0
genap = 0
for angka in list_angka:
    if (angka % 2 == 0):
        genap = genap + 1
    else:
        ganjil = ganjil + 1
print("jumlah bilangan genap: ",genap)
print("jumlah bilangan ganjil: ",ganjil)