temanku = ["Aziz", "Sinta", "Fellix", "Abang", "Afril"]

print("Ini adalah temanku dengan nomor indeks ke-4 adalah ",format(temanku[4]))

print("Semua temanku: ada {} orang" .format(len(temanku)))
for teman in temanku:
    print(teman)
print()
print()
temanku = ["Aziz", "Sinta", "Fellix", "Abang", "Afril"]
temanku.insert(0,"Nizar")
temanku.append("Ferdi")
print("Semua temanku: ada {} orang" .format(len(temanku)))
for teman in temanku:
    print(teman)
print()
print()
daftar_lagu = ["Manusia kuat", "Ingkar"]

lagu_favorit = ["Terlukis indah", "Tentang dirimu"]

semua_lagu = daftar_lagu + lagu_favorit
print(semua_lagu)
print()
print()
lagu_favorit = ["Terlukis indah", "Tentang dirimu"]

ulangi = 5

ulangi_lagu = lagu_favorit * ulangi
print(ulangi_lagu)