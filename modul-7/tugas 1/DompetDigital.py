from Pembayaran import MetodePembayaran

class PembayaranDompet(MetodePembayaran):
    def bayar(self, jumlah: float) -> float:
        diskon = 0.02
        return jumlah * (1 - diskon)
