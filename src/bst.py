class BSTNode:

    def __init__(self, mahasiswa):

        self.mahasiswa = mahasiswa
        self.left = None
        self.right = None


class BSTMahasiswa:

    def __init__(self):

        self.root = None

    # =========================
    # INSERT MAHASISWA
    # =========================

    def insert(self, mahasiswa):

        self.root = self._insert(
            self.root,
            mahasiswa
        )

    def _insert(self, node, mahasiswa):

        if node is None:

            return BSTNode(mahasiswa)

        if mahasiswa.nim < node.mahasiswa.nim:

            node.left = self._insert(
                node.left,
                mahasiswa
            )

        else:

            node.right = self._insert(
                node.right,
                mahasiswa
            )

        return node

    # =========================
    # SEARCH MAHASISWA
    # =========================

    def search(self, nim):

        return self._search(
            self.root,
            nim
        )

    def _search(self, node, nim):

        if node is None:

            return None

        if nim == node.mahasiswa.nim:

            return node.mahasiswa

        if nim < node.mahasiswa.nim:

            return self._search(
                node.left,
                nim
            )

        return self._search(
            node.right,
            nim
        )

    # =========================
    # INORDER TRAVERSAL
    # =========================

    def inorder(self):

        self._inorder(self.root)

    def _inorder(self, node):

        if node is not None:

            self._inorder(node.left)

            print(
                "NIM  :",
                node.mahasiswa.nim
            )

            print(
                "Nama :",
                node.mahasiswa.nama
            )

            print(
                "IPK  :",
                round(node.mahasiswa.ipk, 2)
            )

            print("---------------------------")

            self._inorder(node.right)