class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu_darat(self):
        if self.jenis_kendaraan.lower() == "truk":
            return 7
        elif self.jenis_kendaraan.lower() == "motor":
            return 4
        else:
            return 6

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu_udara(self):
        if self.maskapai.lower() == "garuda":
            return 2
        elif self.maskapai.lower() == "lion air":
            return 3
        else:
            return 4

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan)
        udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai)

        estimasi_awal = min(darat.estimasi_waktu_darat(), udara.estimasi_waktu_udara())


        tujuan_domestik = ["jakarta", "bandung", "surabaya"]
        if self.tujuan.lower() not in tujuan_domestik:
            return estimasi_awal + 3
        return estimasi_awal

pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "truk", "Garuda")
pengiriman2 = PengirimanInternasional("Bandung", "Surabaya", "motor", "Lion Air")
pengiriman3 = PengirimanInternasional("Medan", "Tokyo", "mobil", "Emirates")

print(f"Estimasi pengiriman 1: {pengiriman1.estimasi_waktu()} hari, {pengiriman1.PengirimanInternasional()}")
print(f"Estimasi pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi pengiriman 3: {pengiriman3.estimasi_waktu()} hari")

