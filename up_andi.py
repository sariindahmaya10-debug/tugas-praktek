
print("=== PENILAIAN MAHASISWA ===")

jumlah = int(input("Jumlah mahasiswa: "))

lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama: ")
    nilai = int(input("Nilai: "))

    if nilai >= 85:
        grade = "A - Sangat Baik"
        lulus += 1
    elif nilai >= 75:
        grade = "B - Baik"
        lulus += 1
    elif nilai >= 60:
        grade = "C - Cukup"
        lulus += 1
    else:
        grade = "D - Tidak Lulus"
        tidak_lulus += 1

    print("Nama:", nama)
    print("Hasil:", grade)

print("\n=== HASIL AKHIR ===")
print("Jumlah mahasiswa:", jumlah)
print("Mahasiswa lulus:", lulus)
print("Tidak lulus:", tidak_lulus)

print("=== PROGRAM SELESAI ===")
