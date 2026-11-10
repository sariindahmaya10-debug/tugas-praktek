print("=== SISTEM PENILAIAN MAHASISWA ===")

jumlah = int(input("Masukkan jumlah mahasiswa (1-5): "))

if jumlah >= 1 and jumlah <= 5:
    total = 0

    for i in range(1, jumlah + 1):
        print("\nMahasiswa ke-", i)

        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))

        total = total + nilai

        if nilai >= 75:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        print("Nama   :", nama)
        print("Nilai  :", nilai)
        print("Status :", status)

    rata_rata = total / jumlah

    print("\n=== HASIL PENILAIAN ===")
    print("Jumlah mahasiswa :", jumlah)
    print("Total nilai      :", total)
    print("Nilai rata-rata  :", rata_rata)

else:
    print("Jumlah mahasiswa harus 1 sampai 5!")