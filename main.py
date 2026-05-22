from src.data_structures.bst import BSTMahasiswa
from src.data_structures.stack import Stack
from src.data_structures.graph import Graph
from src.data_structures.queue import Queue
from src.data_structures.sorting import bubble_sort
from src.data_structures.doubly_linked_list import DoublyLinkedList

from models.mahasiswa import Mahasiswa
from models.nilai import Nilai

# ======================================
# INISIALISASI STRUKTUR DATA
# ======================================

bst = BSTMahasiswa()
undo_stack = Stack()
graph = Graph()

queue = Queue()

dll = DoublyLinkedList()

# ======================================
# DATA GRAPH PRASYARAT
# ======================================

daftar_mk = [
    "ELT101",
    "ELT201",
    "ELT301",
    "INF101",
    "INF201"
]

for mk in daftar_mk:
    graph.tambah_mk(mk)

graph.tambah_prasyarat("ELT101", "ELT201")
graph.tambah_prasyarat("ELT201", "ELT301")
graph.tambah_prasyarat("INF101", "INF201")

# ======================================
# FUNCTION FILTER IPK
# ======================================

def filter_ipk(node, bawah, atas):

    if node is not None:

        filter_ipk(node.left, bawah, atas)

        if bawah <= node.mahasiswa.ipk <= atas:

            print("--------------------------------")
            print("NIM  :", node.mahasiswa.nim)
            print("Nama :", node.mahasiswa.nama)
            print("IPK  :", round(node.mahasiswa.ipk, 2))

        filter_ipk(node.right, bawah, atas)

# ======================================
# FUNCTION AMBIL DATA
# ======================================

def ambil_data(node, data):

    if node is not None:

        ambil_data(node.left, data)

        data.append(node.mahasiswa)

        ambil_data(node.right, data)

# ======================================
# PROGRAM UTAMA
# ======================================

while True:

    print("\n===================================")
    print(" STUDENT ACADEMIC PERFORMANCE ")
    print("===================================")

    print("1. Tambah Mahasiswa")
    print("2. Cari Mahasiswa")
    print("3. Tambah Nilai")
    print("4. Tampilkan Transkrip")
    print("5. Undo Nilai")
    print("6. Tampilkan Semua Mahasiswa")
    print("7. Tampilkan Graph Prasyarat")
    print("8. Filter IPK")
    print("9. Ranking IPK")
    print("10. Tampilkan Queue")
    print("11. Keluar")

    pilih = input("Pilih menu : ")

    # ======================================
    # 1. TAMBAH MAHASISWA
    # ======================================

    if pilih == "1":

        nim = input("Masukkan NIM  : ")
        nama = input("Masukkan Nama : ")

        cek_mahasiswa = bst.search(nim)

        if cek_mahasiswa is not None:

            print("NIM sudah terdaftar")

        else:

            mahasiswa = Mahasiswa(nim, nama)

            bst.insert(mahasiswa)

            queue.enqueue(nama)

            dll.append(nama)

            print("Mahasiswa berhasil ditambahkan")

    # ======================================
    # 2. CARI MAHASISWA
    # ======================================

    elif pilih == "2":

        nim = input("Masukkan NIM : ")

        mahasiswa = bst.search(nim)

        if mahasiswa is not None:

            print("\n===== DATA MAHASISWA =====")
            print("NIM  :", mahasiswa.nim)
            print("Nama :", mahasiswa.nama)
            print("IPK  :", round(mahasiswa.ipk, 2))

        else:

            print("Mahasiswa tidak ditemukan")

    # ======================================
    # 3. TAMBAH NILAI
    # ======================================

    elif pilih == "3":

        nim = input("Masukkan NIM : ")

        mahasiswa = bst.search(nim)

        if mahasiswa is not None:

            kode_mk = input("Kode MK  : ")
            semester = int(input("Semester : "))
            grade = input("Grade     : ").upper()

            daftar_grade = [
                "A", "A-",
                "B+", "B", "B-",
                "C+", "C",
                "D", "E"
            ]

            if grade not in daftar_grade:

                print("Grade tidak valid")

            else:

                nilai = Nilai(
                    kode_mk,
                    semester,
                    grade
                )

                mahasiswa.tambah_nilai(nilai)

                undo_stack.push((nim, nilai))

                print("Nilai berhasil ditambahkan")
                print("IPK terbaru :", round(mahasiswa.ipk, 2))

        else:

            print("Mahasiswa tidak ditemukan")

    # ======================================
    # 4. TAMPILKAN TRANSKRIP
    # ======================================

    elif pilih == "4":

        nim = input("Masukkan NIM : ")

        mahasiswa = bst.search(nim)

        if mahasiswa is not None:

            print("\n===== TRANSKRIP =====")
            print("NIM  :", mahasiswa.nim)
            print("Nama :", mahasiswa.nama)

            mahasiswa.tampilkan_transkrip()

        else:

            print("Mahasiswa tidak ditemukan")

    # ======================================
    # 5. UNDO NILAI
    # ======================================

    elif pilih == "5":

        if undo_stack.is_empty():

            print("Tidak ada data undo")

        else:

            data_undo = undo_stack.pop()

            nim = data_undo[0]

            mahasiswa = bst.search(nim)

            if mahasiswa is not None:

                mahasiswa.hapus_nilai_terakhir()

                print("Undo nilai berhasil")
                print("IPK terbaru :", round(mahasiswa.ipk, 2))

    # ======================================
    # 6. TAMPILKAN SEMUA MAHASISWA
    # ======================================

    elif pilih == "6":

        print("\n===== DATA MAHASISWA =====")

        bst.inorder()

    # ======================================
    # 7. TAMPILKAN GRAPH PRASYARAT
    # ======================================

    elif pilih == "7":

        print("\n===== GRAPH PRASYARAT =====")

        graph.tampilkan()

    # ======================================
    # 8. FILTER IPK
    # ======================================

    elif pilih == "8":

        bawah = float(input("IPK minimum : "))
        atas = float(input("IPK maksimum : "))

        print("\n===== HASIL FILTER IPK =====")

        filter_ipk(bst.root, bawah, atas)

    # ======================================
    # 9. RANKING IPK
    # ======================================

    elif pilih == "9":

        data_mahasiswa = []

        ambil_data(bst.root, data_mahasiswa)

        ranking = bubble_sort(data_mahasiswa)

        print("\n===== RANKING IPK =====")

        for mhs in ranking:

            print(
                mhs.nim,
                "-",
                mhs.nama,
                "- IPK:",
                round(mhs.ipk, 2)
            )

    # ======================================
    # 10. TAMPILKAN QUEUE
    # ======================================

    elif pilih == "10":

        print("\n===== QUEUE MAHASISWA =====")

        queue.display()

    # ======================================
    # 11. KELUAR
    # ======================================

    elif pilih == "11":

        print("Program selesai")

        break

    # ======================================
    # MENU TIDAK VALID
    # ======================================

    else:

        print("Menu tidak valid")