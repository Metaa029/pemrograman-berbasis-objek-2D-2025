from peminjaman import BisaDipinjam
from reservasi import BisaDireservasi

class BukuFiksi(BisaDipinjam, BisaDireservasi):
    def pinjam(self) -> None:
        print("Buku fiksi berhasil dipinjam.")

    def reservasi(self) -> None:
        print("Buku fiksi berhasil direservasi.")
