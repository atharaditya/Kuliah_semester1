a = int(input("Masukan angka awal: "))
b = int(input("Masukan angka akhir: "))
for i in range(a,b):
    if i % i == 0 and i % 2 != 0 and i % 3 != 0 or i == 2 or i == 3:
        print(i)