import os
os.system("cls")

nama_mhs = ["Aswin", "Sinta", "Fellix"]
nim = [3202216113,3202216050,3202216107]
usia = [19,19,18]
jenis_klmn = ["Laki-laki", "Perempuan", "Laki-laki"]
print("Nama Mahasiswa\t\t\tNIM\t\tUsia\t\tJenis Kelamin")
for i in range(len(nama_mhs)):
    print(nama_mhs[i],"\t\t\t", nim[i],"\t\t",usia[i],"\t\t",jenis_klmn[i])