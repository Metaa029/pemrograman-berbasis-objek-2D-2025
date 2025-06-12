from reservasi import BisaDireservasi

class BukuReferensi(BisaDireservasi):
    def pinjam(self) -> None:
        print("MAAFFF, Buku referensi TIDAK boleh dipinjam yaa!")

    def reservasi(self) -> None:
        print("Buku referensi berhasil direservasi.")
