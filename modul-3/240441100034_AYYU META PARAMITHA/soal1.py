class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

 
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap\n")


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja}")
        print("Status: Karyawan Harian\n")


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()


manajemen = ManajemenKaryawan()

manajemen.tambah_karyawan(KaryawanTetap("Farhan", 7000000, "IT", 1500000))
manajemen.tambah_karyawan(KaryawanTetap("Bima", 8000000, "HR", 1200000))
manajemen.tambah_karyawan(KaryawanTetap("Jois", 7000000, "IT", 1500000))

manajemen.tambah_karyawan(KaryawanHarian("Arzha", 100000, "Produksi", 8))
manajemen.tambah_karyawan(KaryawanHarian("Irsyad", 120000, "Gudang", 10))
manajemen.tambah_karyawan(KaryawanHarian("Rifki", 100000, "Produksi", 8))

manajemen.tampilkan_semua_karyawan()
