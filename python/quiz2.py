#program A
def score_to_grade(nilai_huruf):
    if nilai_huruf >= 80.51:
        return 'A'
    elif nilai_huruf >= 65.51:
        return 'B'
    elif nilai_huruf >= 50.51:
        return 'C'
    elif nilai_huruf >= 34.41:
        return 'D'
    else:
        return 'E'
    
def calculate_average(nilai_akhir):
    total = sum(nilai_akhir)
    average = total / len(nilai_akhir)
    return average

mahasiswa = [
    ['MUHAMAD ARDALEPA', [89, 93.9, 87.5, 80.0, 85.92]],
    ['UTIN DYAH AYU FEBRIANTI NINGRUM', [55, 67.0, 75.0, 56.0, 63.80]],
    ['PUTRI SARI', [100, 92.7, 90.0, 99.0, 95.13]],
    ['YOGI RESTU DWI PRASETYO', [35, 40.0, 56.0, 79.0, 59.90]],
    ['MUHAMMAD FIKRI HAIKAL', [78, 75.0, 80.0, 78.0, 77.98]],
    ['FAJAR BAYU KRISNA', [89, 92.2, 85.0, 99.0, 92.43]],
    ['RESTU ANUGERAH', [65, 65.0, 76.0, 73.0, 71.50]],
    ['MEISI ARSELIA', [45, 25.0, 35.0, 45.0, 38.00]],
    ['DIAH AYU PUSPITA WARDANI', [100, 93.2, 87.5, 93.2, 92.22]],
    ['DEWI RAMADHANTI', [100, 93.6 ,90.0, 99.0, 95.31]],
    ['NADILA PUTRI',[100, 77.0, 92.5, 99.0, 80.00]],
    ['MUHAMMAD ROBBY ALFIAN',[100, 94.3, 90.0, 99.0, 95.47]],
    ['ANJANI BUNGA SEPTIANDINI',[100, 94.2, 95.0, 90.0, 93.34]],
    ['SYAHWALA PUTRI ADETYA',[100, 95.9, 95.0, 93.3, 92.80]],
    ['BENTO BONGKAR NASUTION',[45, 56.0, 45.0, 46.0, 47.60]],
    ['MUHAMMAD RIZKY IKHSAN PRATAMA',[100, 96.1, 87.5, 93.3, 92.80]],
    ['ADHIETYA IRWANDA',[100, 78.9, 80.0, 93.3, 87.11]],
    ['ANDRE BIRRUL ALIM',[33	,65.0,	75.0,	70.0,	66.83]],
    ['LINTANG KARENINA APRILLIANTI',[78, 91.8, 92.5, 99.0, 93.48]],
    ['MUHAMMAD HAFIDZ SYAH',[22, 0.0, 0.0, 0.0,	2.22]],
    ['RIZKY ALRINO MURTADHO',[89, 94.1, 92.5, 90.0,	91.45]],
    ['RICKY INZAGI BARYONO',[45, 94.3,	56.0,	38.0,	55.37]],
    ['DICKY RIVALDI',[67, 81.1, 87.5, 99.0, 88.74]],
    ['ANANDA PUTRA SYAFAAT',[89, 93.6, 92.5, 90.0, 91.34]],
    ['RIDHO AL FIKRI',[35, 67.0, 45.0, 55.0, 52.40]],
    ['ANDRA ZALIANTY',[100,	93.7,	95.0,	96.7,	95.90]],
    ['NELA SRY DEVI SITOMPUL',[89,	80.0,	75.0,	72.0,	76.20]],
    ['AHMAD LAZUARDI',[100, 92.9, 77.5, 99.0, 91.43]],
    ['IQBAL DWI NUGROHO',[100, 93.6, 85.0, 99.0, 93.81]],
    ['FIRNOVALIA NOVA NOVENA DE CHRISTEA MIYAK',[45, 65.6, 75.0, 61.0, 64.51]]
]

for item in mahasiswa:
    nama = item[0]
    scores = item[1]
    average = calculate_average(scores)
    nilai = score_to_grade(average)
    print(f'{nama}: {average}, {nilai}')

print()    

#program B
import os
os.system('cls')
# Program descending Nama mahasiswa berdasarkan nilai tertinggi
mahasiswa = [
    ("MUHAMAD ARDALEPA", 85.92), 
    ("UTIN DYAH AYU FEBRIANTI NINGRUM", 63.8), 
    ("PUTRI SARI", 95.13), 
    ("YOGI RESTU DWI PRASETYO", 59.9), 
    ("MUHAMMAD FIKRI HAIKAL", 77.98), 
    ("FAJAR BAYU KRISNA", 92.43), 
    ("RESTU ANUGERAH", 71.5), 
    ("MEISI ARSELIA", 38.0), 
    ("DIAH AYU PUSPITA WARDANI", 92.22), 
    ("DEWI RAMADHANTI", 95.31), 
    ("NADILA PUTRI", 80.0), 
    ("MUHAMMAD ROBBY ALFIAN", 95.47), 
    ("ANJANI BUNGA SEPTIANDINI", 93.34), 
    ("SYAHWALA PUTRI ADETYA", 95.01), 
    ("BENTO BONGKAR NASUTION", 47.6), 
    ("MUHAMMAD RIZKY IKHSAN PRATAMA", 92.8), 
    ("ADHIETYA IRWANDA", 87.11), 
    ("ANDRE BIRRUL ALIM", 66.83), 
    ("LINTANG KARENINA APRILLIANTI", 93.48), 
    ("MUHAMMAD HAFIDZ SYAH", 2.22), 
    ("RIZKY ALRINO MURTADHO", 91.45), 
    ("RICKY INZAGI BARYONO", 55.37), 
    ("DICKY RIVALDI", 88.74), 
    ("ANANDA PUTRA SYAFAAT", 91.34), 
    ("RIDHO AL FIKRI", 52.4), 
    ("ANDRA ZALIANTY", 95.9), 
    ("NELA SRY DEVI SITOMPUL", 76.2), 
    ("AHMAD LAZUARDI", 91.43), 
    ("IQBAL DWI NUGROHO", 93.81), 
    ("FIRNOVALIA NOVA NOVENA DE CHRISTEA MIYAK", 64.51),
]

mahasiswa.sort(key=lambda x: x[1], reverse=True)
print()
print("Data yang sudah terurut secara descending :")
print('='*50)
for nama, nilai in mahasiswa:
    print(nama, nilai)

print()    

#program C
import os
os.system('cls')

def count_grades(mahasiswa):
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for line in mahasiswa.split("\n"):
        if line:
            grade = line.split()[-1]
            grades[grade] += 1
    return grades

mahasiswa = """MUHAMAD ARDALEPA  89  93,9    87,5    80,0    85,92   A, UTIN DYAH AYU FEBRIANTI NINGRUM 55  67,0    75,0    56,0    63,80   C
PUTRI SARI  100 92,7    90,0    99,0    95,13   A, YOGI RESTU DWI PRASETYO 35  40,0    56,0    79,0    59,90   C
MUHAMMAD FIKRI HAIKAL   78  75,0    80,0    78,0    77,98   B, FAJAR BAYU KRISNA   89  92,2    85,0    99,0    92,43   A
RESTU ANUGERAH  65  65,0    76,0    73,0    71,50   B, MEISI ARSELIA   45  25,0    35,0    45,0    38,00   D
DIAH AYU PUSPITA WARDANI    100 93,2    87,5    93,3    92,22   A, DEWI RAMADHANTI 100 93,6    90,0    99,0    95,31   A
NADILA PUTRI    100 77,0    92,5    99,0    80,00   B, MUHAMMAD ROBBY ALFIAN   100 94,3    90,0    99,0    95,47   A
ANJANI BUNGA SEPTIANDINI    100 94,2    95,0    90,0    93,34   A, SYAHWALA PUTRI ADETYA   100 95,9    95,0    93,3    95,01   A
BENTO BONGKAR NASUTION  45  56,0    45,0    46,0    47,60   D, MUHAMMAD RIZKY IKHSAN PRATAMA   100 96,1    87,5    93,3    92,80   A
ADHIETYA IRWANDA    100 78,9    80,0    93,3    87,11   A, ANDRE BIRRUL ALIM   33  65,0    75,0    70,0    66,83   B
LINTANG KARENINA APRILLIANTI    78  91,8    92,5    99,0    93,48   A, MUHAMMAD HAFIDZ SYAH    22  0,0 0,0 0,0 2,22    E"""

print()
grades = count_grades(mahasiswa)
for grade, count in grades.items():
    print(f"Jumlah mahasiswa yang mendapatkan nilai A,B,C,D dan E = ",grades)

print()    

#program D
mahasiswa = [    ["MUHAMAD ARDALEPA", "A"],
    ["UTIN DYAH AYU FEBRIANTI NINGRUM", "C"],
    ["PUTRI SARI", "A"],
    ["YOGI RESTU DWI PRASETYO", "C"],
    ["MUHAMMAD FIKRI HAIKAL", "B"],
    ["FAJAR BAYU KRISNA", "A"],
    ["RESTU ANUGERAH", "B"],
    ["MEISI ARSELIA", "D"],
    ["DIAH AYU PUSPITA WARDANI", "A"],
    ["DEWI RAMADHANTI", "A"],
    ["NADILA PUTRI", "B"],
    ["MUHAMMAD ROBBY ALFIAN", "A"],
    ["ANJANI BUNGA SEPTIANDINI", "A"],
    ["SYAHWALA PUTRI ADETYA", "A"],
    ["BENTO BONGKAR NASUTION", "D"],
    ["MUHAMMAD RIZKY IKHSAN PRATAMA", "A"],
    ["ADHIETYA IRWANDA", "A"],
    ["ANDRE BIRRUL ALIM", "B"],
    ["LINTANG KARENINA APRILLIANTI", "A"],
    ["MUHAMMAD HAFIDZ SYAH", "E"],
    ["RIZKY ARLINO MURTHADO", "A"],
    ["RICKY INZAGI BARYONO", "C"],
    ["DICKY RIVALDI ", "A"],
    ["ANANDA PUTRA SYAFAAT ", "A"],
    ["RIDHO AL FIKRI ", "C"]
]

hasil = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
}

for item in mahasiswa:
    hasil[item[1]].append(item[0])

for key, value in hasil.items():
    print(f"Nama mahasiswa dengan nilai {key}:")
    for name in value:
        print(f"- {name}")
    print()