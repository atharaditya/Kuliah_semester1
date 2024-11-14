#meggunakan tipe data set
#tipe data set menggunakan kurung kurawal {}
print(">>>>>> set dengan kurung kurawal")
newprov = {"Papua Tengah","Papua Pegunungan","Papua Selatan","Papua Barat Daya"}
print(newprov)

#mengkonversi list ke dalam set
print(">>>>> konversi list ke dalam set")
gugusan_pulau = set(["Sumatra","Jawa","Kalimantan","Sulawesi","Maluku","Papua"])
print(gugusan_pulau)

#set dengan tipe data yang berbeda-beda
print(">>>> set dengan tipe data yang berbeda-beda")
set_campuran = {"Mahasiswa","Teknik Informatika",3,True,("A","B")}
print(set_campuran)
print()
print()
#kita bisa menjadikan tuple sebagai anggota
#karena ia bersifat imutable
papan_ketik = {
(1,2,3),
(4,5,6),
(7,8,9),
(0)
}
print()
print()
lagu_guruku = set([
    "pagi","ku","cerah","ku","matahari","bersinar","ku"
    "gendong","tas","merah","ku","dipundak"
])
print("Mencetak kata unik dalam list yang di konversi menjadi Set lagu Guruku")
print(lagu_guruku)
print()
print()
#menggunakan fungsi add dan update pada tipe data set
huruf_abjad = {"a","b","c","d","e"}
print("Anggota set data awal.\n",huruf_abjad)

#menambah data dalam set satu per satu
huruf_abjad.add("f")
huruf_abjad.add("g")

#menambah data dalam set lebih dari satu anggota sekaligus
#menambah dengan data set
huruf_abjad.update({"h","i"})
#menambah dengan data list
huruf_abjad.update(["j","k"])

print("\nAnggota Set setelah di berifungsi add dan update.",huruf_abjad)
