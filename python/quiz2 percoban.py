nilai = {"aktivitas": 10, "tugas": 20, "UTS": 30, "UAS": 40}
nilai_range = {"E": (0, 34.50), "D": (34.41, 50.50), "C": (50.51, 65.50), "B": (65.51, 80.50), "A": (80.51, 100)}
mahasiswa = [{"nama": "muhammad ardalepa", "aktivitas": 89, "tugas": 93.9, "UTS": 87, "UAS": 80},
            {"nama": "utin dyah ayu febrianti ningrum", "aktivitas": 55, "tugas": 67, "UTS": 75, "UAS": 63},
            {"nama": "putri sari", "aktivitas": 100, "tugas": 92, "UTS": 99, "UAS":95},
            {"nama": "yogi restu dwi prasetyo", "aktivitas": 35, "tugas": 40, "UTS": 56, "UAS": 79},
            {"nama": "muhamad fikri haikal", "aktivitas": 78, "tugas": 75, "UTS": 80, "UAS": 78},
            {"nama": "fajar bayu krisna", "aktivitas": 89, "tugas": 92, "UTS": 85, "UAS": 99},
            ]
for mhs in mahasiswa:
    total_nilai = 0
    for component, grade in mhs.items():
        if component in nilai:
            total_nilai += (grade * nilai[component]) / 100
    mhs["nilai_akhir"] = total_nilai
    mhs["nilai_huruf"] = None
    for letter, grade_r in nilai_range.items():
        if mhs["nilai_akhir"] >= grade_r[0] and mhs["nilai_akhir"] <= grade_r[1]:
            mhs["nilai_huruf"] = letter
            break
mahasiswa = sorted(mahasiswa, key=lambda x: x["nilai_akhir"], reverse=True)
print("Sort mahasiswa secara descending:")
for mhs in mahasiswa:
    print(f"Nama: {mhs['nama']},\t\t nilai_akhir: {mhs['nilai_akhir']}, \t\tnilai_huruf: {mhs['nilai_huruf']}")
