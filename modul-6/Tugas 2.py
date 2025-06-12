from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, gaji_pokok, tunjangan):
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
    
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, upah_per_jam, jam_kerja):
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    
    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

def cetak_gaji(karyawan):
    print(f"Total gaji: Rp {karyawan.hitung_gaji()}")

def main():
    print("\n===== Program Menghitung Gaji Karyawan =====")
    print("[1] Karyawan Tetap")
    print("[2] Karyawan Kontrak")
    print("============================================")

    
    pilihan = int(input("\nPilih jenis karyawan (1-2): "))
    
    if pilihan == 1:
        gaji_pokok = int(input("Masukkan gaji pokok: Rp "))
        tunjangan = int(input("Masukkan tunjangan: Rp "))
        karyawan = KaryawanTetap(gaji_pokok, tunjangan)
    elif pilihan == 2:
        upah_per_jam = int(input("Masukkan upah per jam: Rp "))
        jam_kerja = int(input("Masukkan total jam kerja: "))
        karyawan = KaryawanKontrak(upah_per_jam, jam_kerja)
    else:
        print("Pilihan tidak valid!")
        return
    
    cetak_gaji(karyawan)

main()