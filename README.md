# tpb-asd-student-akademic-perfomance-tracker-kel03

## Student Academic Performance Tracker

Project ini merupakan aplikasi pengelolaan data akademik mahasiswa berbasis Python menggunakan struktur data Binary Search Tree (BST), Stack, dan Graph. Sistem dibuat berbasis Command Line Interface (CLI) untuk membantu proses penyimpanan, pencarian, dan pengelolaan data mahasiswa secara lebih terstruktur dan efisien.

---

## Fitur Program

- Tambah data mahasiswa
- Cari data mahasiswa berdasarkan NIM
- Tambah nilai mahasiswa
- Tampilkan transkrip nilai
- Undo nilai menggunakan Stack
- Filter IPK mahasiswa
- Ranking IPK mahasiswa
- Statistik grade mahasiswa
- Graph prasyarat mata kuliah

---

## Struktur Data yang Digunakan

### 1. Binary Search Tree (BST)
Digunakan untuk:
- Menyimpan data mahasiswa
- Mencari data mahasiswa berdasarkan NIM

### 2. Stack
Digunakan untuk:
- Fitur undo nilai mahasiswa

### 3. Graph
Digunakan untuk:
- Menampilkan hubungan prasyarat mata kuliah

---

## Struktur Folder Project

```text
tpb-asd-student-akademic-perfomance-tracker-kel03/
│
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── bst.py
│   ├── stack.py
│   └── graph.py
│
├── models/
│   ├── __init__.py
│   ├── mahasiswa.py
│   └── nilai.py
│
├── AI_Log/
│   ├── Log_prompt.txt
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── Link_GPT.txt
│
├── docs/
│   ├── laporan.pdf
│   └── slide_presentasi.pptx
│
├── tests/
│   ├── test_bst.py
│   ├── test_stack.py
│   └── test_graph.py
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   │
│   └── pull_request_template.md
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Cara Menjalankan Program

### 1. Clone Repository

```bash
git clone https://github.com/Alfintio-byte/tpb-asd-student-akademic-perfomance-tracker-kel03.git
```

### 2. Masuk ke Folder Project

```bash
cd tpb-asd-student-akademic-perfomance-tracker-kel03
```

### 3. Jalankan Program

```bash
python main.py
```

---

## Analisis Big-O

| Operasi | Struktur Data | Kompleksitas |
|---|---|---|
| Insert Mahasiswa | BST | O(log n) |
| Search Mahasiswa | BST | O(log n) |
| Push Undo | Stack | O(1) |
| Pop Undo | Stack | O(1) |
| Tambah Edge | Graph | O(1) |

---

## Teknologi yang Digunakan

- Python 3
- GitHub
- Visual Studio Code

---

## Anggota Kelompok

- Nama Anggota 1
- Nama Anggota 2
- Nama Anggota 3
- Nama Anggota 4

---

## Dokumentasi

- Laporan project terdapat pada folder `docs/`
- Log penggunaan AI terdapat pada folder `AI_Log/`

---

## Kesimpulan

Project ini berhasil mengintegrasikan beberapa struktur data seperti BST, Stack, dan Graph ke dalam sebuah aplikasi pengelolaan data akademik mahasiswa berbasis CLI. Sistem dapat digunakan untuk membantu proses penyimpanan, pencarian, dan pengolahan data mahasiswa secara lebih efisien dan terstruktur.