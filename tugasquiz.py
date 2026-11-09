#----input----
nama = input("masukkan nama mahasiswa:")
mahasiswa = ("andi","budi","citra")
Target = ("70,75,80")
#----proses---
if nama == "andi" :
    Target = 70
elif nama == "budi" :
    Target = 75
elif nama == "citra":
    Target = 80
else :
    Target = 0
if Target == 0:
    print("nama mahasiswa tidak ditemukan!")
else:
    print("target nilai",nama,"adalah",Target)

    percobaan = 1
    while percobaan <= 3:
        nilai = int(input("masukkan nilai:"))
        if nilai >= Target:
            print(nama,"berhasil lulus!")
            print("setelah", percobaan,"kali percobaan")
            break
        else:
            print("nilai belum mencapai target!")
            percobaan=percobaan +  1
    if percobaan > 3:
        print(nama,"dinyatakan tidak lulus setelah 3 kali percobaan!")
