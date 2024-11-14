kumpulan = {'manggis','mangga','150',('x','y'),False,True}
print(kumpulan)

#menggunakan fungsi remove() nilai set, tidak error jika nilai ada dalam set
kumpulan.remove('150')
print(kumpulan)
#menggunakan fungsi remove() nilai set, error jika nilai tidak ada dalam set
kumpulan.remove('200')
print(kumpulan)

#menggunakan fungsi discard() nilai set, tidak error jika nilai ada dalam set
kumpulan.remove(('x','y'))
print(kumpulan)

#menggunakan fungsi pop nilai yang ada di sebelah kiri
kumpulan.pop()
print(kumpulan)

#menggunakan fungsi clear() untuk menghapus seluruh nilai set
kumpulan.clear()
print(kumpulan)