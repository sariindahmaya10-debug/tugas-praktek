# =====================================
# PROGRAM SISTEM EVALUASI MAHASISWA
#  tugas praktikum Algoritma dan Pemrograman Python
# =====================================

print("===================================")
print("     SISTEM EVALUASI MAHASISWA")
print("===================================")

# 1. Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# 2. Menghitung nilai akhir
nilai_akhir = (20 * tugas / 100) + (30 * uts / 100) + (50 * uas / 100)

# 3. Menampilkan hasil perhitungan
print("\n========== HASIL EVALUASI ==========")
print("Nama mahasiswa :", nama)
print("Nilai tugas    :", tugas)
print("Nilai UTS      :", uts)
print("Nilai UAS      :", uas)
print("Kehadiran      :", kehadiran, "%")
print("Nilai akhir    :", round(nilai_akhir, 2))

# 4. Menentukan status kelulusan
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status         : LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status         : LULUS")
else:
    print("Status         : BELUM LULUS")

print("====================================")