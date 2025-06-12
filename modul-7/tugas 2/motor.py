from booking import BookingKendaraan
from biaya import BiayaKendaraan
from asuransi import AsuransiKendaraan

class Motor(BookingKendaraan, BiayaKendaraan, AsuransiKendaraan):
    def pesan(self, usia: int) -> bool:
        if usia < 18:
            print("MAAF, Usia minimal untuk menyewa motor adalah 18 tahun.")
            return False
        print("SELAMATTT, Motor berhasil dipesan.")
        return True

    def hitung_biaya(self) -> float:
        return 100_000

    def biaya_asuransi(self) -> float:
        return 20_000
