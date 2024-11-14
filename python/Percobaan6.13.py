import os
os.system("cls")

nama_mhs = ["Adil", "Atha", "Ferry", "Erick", "Iqbal", "Sinta", "Akram", "Fellix", "Afril", "Afif"]
nim = [3202216005,3202216006,3202216011,3202216014,3202216017,3202216050,3202216053,3202216107,3202216058,3202216059]
usia = [18,18,18,18,18,19,18,18,18,18]
jenis_klmn = ["Laki-laki", "Laki-laki", "Laki-laki", "Laki-laki", "Laki-laki", "Perempuan", "Laki-laki",
"Laki-laki", "Laki-laki", "Laki-laki"]
print("Nama Mahasiswa\t\tNIM\t\tUsia\t\tJenis Kelamin")

for i in range(len(nama_mhs)):
    print(nama_mhs[i],"\t\t",nim[1],"\t\t",usia[i],"\t\t",jenis_klmn[i])