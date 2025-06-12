from Pembayaran import MetodePembayaran

class PembayaranKartu(MetodePembayaran):
    def bayar(self, jumlah: float) -> float:
        biaya_tambahan = 0.03
        return jumlah * (1 + biaya_tambahan)
