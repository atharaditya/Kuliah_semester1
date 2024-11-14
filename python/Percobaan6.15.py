import os
os.system("cls")

nama_mhs = ["Adil", "Atha", "Iqbal", "Sinta", "Afril"]
nim = [3202216005,3202216006,3202216017,3202216050,3202216058]
usia = [18,18,18,18,18,19,18,18,18,18]
jenis_klmn = ["Laki-laki", "Laki-laki", "Laki-laki", "Perempuan", "Laki-laki"]
print("Nama Mahasiswa\t\tNIM\t\tUsia\t\tJenis Kelamin")
for i in range(len(nama_mhs)):
    print(nama_mhs[i],"\t\t", nim[i],"\t\t",usia[i],"\t\t",jenis_klmn[i]) 