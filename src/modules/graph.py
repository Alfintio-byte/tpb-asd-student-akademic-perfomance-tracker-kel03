class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_mk(self, mk):
        if mk not in self.graph:
            self.graph[mk] = []

    def tambah_prasyarat(self, mk_awal, mk_tujuan):
        self.graph[mk_awal].append(mk_tujuan)

    def tampilkan(self):
        for mk in self.graph:
            print(mk, "->", self.graph[mk])