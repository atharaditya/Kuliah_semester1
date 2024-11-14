nama = 'Budi'
usia = 20
lajang = True

print(type(nama))
print(type(usia))
print(type(lajang))

print()

usia = input('Masukkan usia anda: ')
print(type(usia))

print()

a = 10 / 2
print(type(a))
b = 1 / 2
print(type(b))

print()

c = 10 + 5 # hasilnya integer
print(type(c))
d = 10 + 5.0 # hasilnya float
print(type(d))
e = 10.5 - 3 # hasilnya float
print(type(e))

print()

kata = 'Jeruk ' * 5
print(kata)
print(type(kata))

print()

panjang = int(input('Masukkan panjang: '))
lebar = float(input('Masukkan lebar: '))
print('Luas =', panjang * lebar)

print()

print(int(5.6))
print(float(5))

print()

nama = 'Wudi'
tahun_lahir = 2000
print(nama + ' lahir di tahun ' + str(tahun_lahir))

print()

print(type(None), '->', bool(None))
print(type(0), '->', bool(0))
print(type(0.0), '->', bool(0.0))
print(type(""), '->', bool(""))
print(type([]), '->', bool([]))
print(type(()), '->', bool(()))
print(type({}), '->', bool({}))

print("-" * 20)

print(type(5), '->', bool(5))
print(type(-14.5), '->', bool(-14.5))
print(type("Aku"), '->', bool("Aku"))
print(type([1, 2, 3]), '->', bool([1, 2, 3]))
print(type(("a", "b", False)), '->', bool(("a", "b", False)))
print(type({ 'nama': 'Lendis Fabri' }), '->', bool({ 'nama': 'Lendis Fabri' }))

print()

# list ke tuple dan ke set
listHuruf = ['a', 'b', 'c', 'c']

print(listHuruf)
print(tuple(listHuruf))
print(set(listHuruf))

print()

# tuple ke list dan ke set
tplBuah = ('Mangga', 'Jambu')
print(tplBuah)
print(list(tplBuah))
print(set(tplBuah))

print()

# set ke list dan ke tuple
setAngka = {1, 3, 5, 5}
print(setAngka)
print(list(setAngka))
print(tuple(setAngka))