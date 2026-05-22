class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_nilai(self, nilai):
        new_node = DLLNode(nilai)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def hapus_terakhir(self):
        if self.tail is None:
            return None

        removed = self.tail

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed.data

    def tampilkan(self):
        current = self.head

        while current:
            n = current.data
            print(f"{n.kode_mk} | Semester {n.semester} | {n.grade}")
            current = current.next