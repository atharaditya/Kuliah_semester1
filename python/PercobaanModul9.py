#percobaan 9.1
#contoh 1
def printme(str):
    'This prints a pssed string into this function'
    print(str)
    return
printme('hello world')
print()
print()
#percobaan 9.2
#contoh 2 penjumlahan sebuah barisan angka
def jumlah(angka):
    total = 0
    for x in angka:
        total += x
    return total

print('jumlah: ',jumlah((8,3,1,4,5)))
print()
print()
#percobaan 9.3
#contoh 3 pengecekan angka apakah ganjil atau genap?
def cek_ganjil_genap(angka):
    if angka%2==0:
        print('genap')
    else:
        print('ganjil')
    return

cek_ganjil_genap(5) #input angka, misalkan 5
print()
print()
#percobaan 9.4
#contoh 4 perhitungan rata-rata
def rata_rata(a,b,c):
    return (a+b+c)/3

print(rata_rata(1,2,3))
print()
print()
#percobaan 9.5
#contoh 5 perhitungan sederhana matematika
def kalkulator(angka1,angka2):
    print(angka1+angka2)
    print(angka1-angka2)
    print(angka1*angka2)
    print(angka1/angka2)

kalkulator(1,2) #inputan 2 angka, angka:1, dan angka2:2