import csv
students = []
def simpan_data():
    file = open("students.csv", "w", newline="")

    writer = csv.writer(file)

    writer.writerow(["Nama", "Rata-rata", "Status"])

    for s in students:
        writer.writerow(s)

    file.close()

while True:
    print("\n=== Student Academic Performance Tracker ===")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Data")
    print("3. Ranking Mahasiswa")
    print("4. Cari Mahasiswa")
    print("5. Hapus Mahasiswa")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama mahasiswa: ")

        tugas = int(input("Nilai tugas: "))
        uts = int(input("Nilai UTS: "))
        uas = int(input("Nilai UAS: "))

        rata = (tugas + uts + uas) / 3

        if rata >= 75:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        students.append([nama, rata, status])
        simpan_data()

    elif pilih == "2":
        print("\n=== DATA MAHASISWA ===")

        for s in students:
            print("Nama :", s[0])
            print("Rata-rata :", s[1])
            print("Status :", s[2])
            print()

    elif pilih == "3":
        print("\n=== RANKING MAHASISWA ===")

        ranking = sorted(students, key=lambda x: x[1], reverse=True)

        nomor = 1

        for s in ranking:
            print(nomor, ".", s[0], "-", s[1])
            nomor += 1

    elif pilih == "4":
        cari = input("Masukkan nama mahasiswa: ")

        ditemukan = False

        for s in students:
            if s[0].lower() == cari.lower():
                print("\nData ditemukan")
                print("Nama :", s[0])
                print("Rata-rata :", s[1])
                print("Status :", s[2])

                ditemukan = True

        if ditemukan == False:
            print("Data tidak ditemukan")

    elif pilih == "5":
        hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")

        ditemukan = False

        for s in students:
            if s[0].lower() == hapus.lower():
                students.remove(s)
                simpan_data()
                print("Data berhasil dihapus")
                ditemukan = True
                break

        if ditemukan == False:
            print("Data tidak ditemukan")

    elif pilih == "6":
        break