students = []

while True:
    print("\n=== Student Academic Performance Tracker ===")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Data")
    print("3. Keluar")

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

    elif pilih == "2":
        print("\n=== DATA MAHASISWA ===")

        for s in students:
            print("Nama :", s[0])
            print("Rata-rata :", s[1])
            print("Status :", s[2])
            print()

    elif pilih == "3":
        break