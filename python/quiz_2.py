mahasiswa = (["MUHAMAD ARDALEPA\t\t\t","UTIN DYAH AYU FEBRIANTI NINGRUM\t","PUTRI SARI\t\t\t\t","YOGI RESTU DWI PRASETYO\t\t","MUHAMMAD FIKRI HAIKAL\t\t\t","FAJAR BAYU KRISNA\t\t\t",
"RESTU ANUGERAH\t\t\t\t","MEISI ARSELIA\t\t\t\t","DIAH AYU PUSPITA WARDANI\t\t","DEWI RAMADHANTI\t\t\t","NADILA PUTRI\t\t\t\t","MUHAMMAD ROBBY ALFIAN\t\t\t","ANJANI BUNGA SEPTIANDINI\t\t",
"SYAHWALA PUTRI ADETYA\t\t\t","BENTO BONGKAR NASUTION\t\t\t","MUHAMMAD RIZKY IKHSAN PRATAMA\t\t","ADHIETYA IRWANDA\t\t\t","ANDRE BIRRUL ALIM\t\t\t","LINTANG KARENINA APRILLIANTI\t\t",
"MUHAMMAD HAFIDZ SYAH\t\t\t","RIZKY ALRINO MURTADHO\t\t\t","RICKY INZAGI BARYONO\t\t\t","DICKY RIVALDI\t\t\t\t","ANANDA PUTRA SYAFAAT\t\t\t","RIDHO AL FIKRI\t\t\t\t","ANDRA ZALIANTY\t\t\t\t","NELA SRY DEVI SITOMPUL\t\t\t",
"AHMAD LAZUARDI\t\t\t\t","IQBAL DWI NUGROHO\t\t\t","FIRNOVALIA NOVA NOVENA DE CHRISTEA MIYAK"
])

# Nilai Mahasiswa
nilai_mahasiswa = [
#nilai aktivitas
    [89,55,10,35,78,89,65,45,10,10,10,10,10,10,45,10,10,33,78,22,89,45,67,89,35,10,89,10,10,45],
#nilai tugas
    [93.9,67.0,92.7,40.0,75.0,92.2,65.0,25.0,93.2,93.6,77.0,94.3,94.2,95.9,56.0,96.1,78.9,65.0,91.8,0.0,94.1,94.3,81.1,93.6,67.0,93.7,80.0,92.9,93.6,65.6,],  
#nilai UTS
    [87.5,75.0,90.0,56.0,80.0,85.0,76.0,35.0,87.5,90.0,92.5,90.0,95.0,95.0,45.0,87.5,80.0,75.0,92.5,0.0,92.5,56.0,87.5,92.5,45.0,95.0,75.0,77.5,85.0,75.0,],  
#Nilai UAS
    [80.0,56.0,99.0,79.0,78.0,99.0,73.0,45.0,93.3,99.0,99.0,99.0,90.0,93.3,46.0,93.3,93.3,70.0,99.0,0.0,90.0,38.0,99.0,90.0,55.0,96.7,72.0,99.0,99.0,61.0,] 
]

# Bobot Nilai
bobot_nilai = [0.1, 0.2, 0.3, 0.4]

# Hitung Nilai Akhir
nilai_akhir = []
for i in range(len(mahasiswa)):
    nilai = 0
    for j in range(len(bobot_nilai)):
        nilai += nilai_mahasiswa[j][i] * bobot_nilai[j]
    nilai_akhir.append(nilai)

# Konversi Nilai Akhir ke Huruf
nilai_huruf = []
for n in nilai_akhir:
    if n >= 80.51:
        nilai_huruf.append('A')
    elif n >= 65.51:
        nilai_huruf.append('B')
    elif n >= 50.51:
        nilai_huruf.append('C')
    elif n >= 34.41:
        nilai_huruf.append('D')
    else:
        nilai_huruf.append('E')

# Urutkan Nilai Tertinggi ke Terendah (Bubble Sort)
for i in range(len(nilai_akhir) - 1, 0, -1):
    for j in range(i):
        if nilai_akhir[j] < nilai_akhir[j+1]:
            nilai_akhir[j], nilai_akhir[j+1] = nilai_akhir[j+1], nilai_akhir[j]
            mahasiswa[j], mahasiswa[j+1] = mahasiswa[j+1], mahasiswa[j]
            nilai_huruf[j], nilai_huruf[j+1] = nilai_huruf[j+1], nilai_huruf[j]

# Hitung Jumlah Nilai A, B, C, D, dan E
nilai_a = nilai_b = nilai_c = nilai_d = nilai_e = 0
for h in nilai_huruf:
    if h == 'A':
        nilai_a += 1
    elif h == 'B':
        nilai_b += 1
    elif h == 'C':
        nilai_c += 1
    elif h == 'D':
        nilai_d += 1
    else:
        nilai_e += 1

# Tampilkan Nama dan Nilai Mahasiswa
index = 0
for item in mahasiswa:
        print("",item,"\t\t\t", round (nilai_akhir[index],1),"\t\t Grade",nilai_huruf[index])
        index += 1

print()
print("jumlah mahasiswa yang mendapatkan nilai A :",nilai_a,"orang")
print("jumlah mahasiswa yang mendapatkan nilai B :",nilai_b,"orang")
print("jumlah mahasiswa yang mendapatkan nilai C :",nilai_c,"orang")
print("jumlah mahasiswa yang mendapatkan nilai D :",nilai_d,"orang")
print("jumlah mahasiswa yang mendapatkan nilai E :",nilai_e,"orang")