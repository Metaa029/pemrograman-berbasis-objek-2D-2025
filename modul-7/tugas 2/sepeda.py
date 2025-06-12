from booking import BookingKendaraan
from biaya import BiayaKendaraan
from asuransi import AsuransiKendaraan

class Sepeda(BookingKendaraan, BiayaKendaraan, AsuransiKendaraan):
    def pesan(self, usia: int) -> bool:
        print("SELAMATTT, Sepeda berhasil dipesan (tanpa batas usia).")
        return True

    def hitung_biaya(self) -> float:
        return 30_000

    def biaya_asuransi(self) -> float:
        return 5_000
