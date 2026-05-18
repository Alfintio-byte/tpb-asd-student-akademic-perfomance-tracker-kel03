class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.ipk = 0.0
        self.transkrip = []

    def tambah_nilai(self, nilai):
        self.transkrip.append(nilai)
        self.hitung_ipk()

    def hapus_nilai_terakhir(self):
        if len(self.transkrip) > 0:
            self.transkrip.pop()
            self.hitung_ipk()

    def hitung_ipk(self):
        if len(self.transkrip) == 0:
            self.ipk = 0.0
            return

        bobot_nilai = {
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "D": 1.0,
            "E": 0.0
        }

        total = 0

        for nilai in self.transkrip:
            total += bobot_nilai.get(nilai.grade, 0)

        self.ipk = total / len(self.transkrip)

    def tampilkan_transkrip(self):
        if len(self.transkrip) == 0:
            print("Belum ada nilai")
            return

        for nilai in self.transkrip:
            print(
                f"{nilai.kode_mk} | Semester {nilai.semester} | Grade {nilai.grade}"
            )

        print(f"IPK : {self.ipk:.2f}")