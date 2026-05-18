students = []

while True:
    print("\n=== Student Academic Performance Tracker ===")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Data")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama mahasiswa: ")
        nilai = int(input("Nilai: "))

        students.append([nama, nilai])

    elif pilih == "2":
        for s in students:
            print("Nama:", s[0], "| Nilai:", s[1])

    elif pilih == "3":
        break