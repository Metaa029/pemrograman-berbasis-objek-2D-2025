from Pembayaran import MetodePembayaran

class PembayaranTunai(MetodePembayaran):
    def bayar(self, jumlah: float) -> float:
        diskon = 0.05
        return jumlah * (1 - diskon)
