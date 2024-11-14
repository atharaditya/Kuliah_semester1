print("QUIZ MENGHITUNG NILAI MAHASISWA")
nama = (input("Masukan Nama Anda	\t: "))
nim = int(input("Masukan NIM Anda	\t: "))
quiz = float(input("Masukan Nilai quiz	\t: "))
tugas = float(input("Masukan Nilai Tugas	\t: "))
uts = float(input("Masukan Nilai UTS	\t: "))
uas = float(input("Masukan Nilai UAS	\t: "))
a = (quiz)*(0.1)
b = (tugas)*(0.2)
c = (uts)*(0.3)
d = (uas)*(0.4)
hasil_akhir = a+b+c+d
print("=====================================")
print("**** KARTU HASIL STUDI MAHASISWA ****")
print("=====================================")
print(f"Nama Mahasiswa  \t: {nama}		NIM \t: {nim}")
print(f"Nilai Quiz      \t: ",a)
print(f"Nilai Tugas     \t: ",b)
print(f"Nilai UTS       \t: ",c)
print(f"Nilai UAS       \t: ",d)
print(f"Nilai akhir anda\t: ",hasil_akhir)
if(hasil_akhir > 80.51):
	print("selamat anda lulus dengan nilai A")
elif(hasil_akhir > 65.51):
	print("selamat anda lulus dengan nilai B")
elif(hasil_akhir > 50.51):
	print("selamat anda lulus dengan nilai C")
elif(hasil_akhir > 40.4):
	print("selamat anda lulus dengan nilai D")
else:
	print("anda tidak lulus")
