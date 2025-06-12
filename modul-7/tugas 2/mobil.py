from booking import BookingKendaraan
from biaya import BiayaKendaraan
from asuransi import AsuransiKendaraan

class Mobil(BookingKendaraan, BiayaKendaraan, AsuransiKendaraan):
    def pesan(self, usia: int) -> bool:
        if usia < 20:
            print("MAAF, Usia minimal untuk menyewa mobil adalah 20 tahun.")
            return False
        print("SELAMATTT, Mobil berhasil dipesan.")
        return True

    def hitung_biaya(self) -> float:
        return 700_000  

    def biaya_asuransi(self) -> float:
        return 50_000
