class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
    
    @property
    def nama(self):
        return self.__nama
    
    @property
    def umur(self):
        return self.__umur
    
    @property
    def keluhan(self):
        return self.__keluhan
    
    def info(self):
        print("\nData Pasien:")
        print(f"Nama: {self.__nama}")
        print(f"Umur: {self.__umur} tahun")
        print(f"Keluhan: {self.__keluhan}")
        print("-" * 30)

class Klinik:
    def __init__(self):
        self.__daftar_pasien = []
    
    def tambah_pasien(self):
        print("\nPendaftaran Pasien Baru")
        nama = input("Masukkan nama pasien: ")
        try:
            umur = int(input("Masukkan umur pasien: "))
            if umur <= 0:
                print("Umur harus lebih dari 0")
                return
        except ValueError:
            print("Umur harus angka")
            return
        
        keluhan = input("Masukkan keluhan: ")
        
        pasien_baru = Pasien(nama, umur, keluhan)
        self.__daftar_pasien.append(pasien_baru)
        print("Pasien berhasil didaftarkan!")
    
    def cari_pasien(self, nama):
        for pasien in self.__daftar_pasien:
            if pasien.nama == nama:
                return pasien
        return None
    
    def tampilkan_semua_pasien(self):
        if not self.__daftar_pasien:
            print("\nBelum ada pasien terdaftar")
            return
        
        print("\nDaftar Pasien:")
        for i, pasien in enumerate(self.__daftar_pasien, 1):
            print(f"{i}. {pasien.nama} - {pasien.umur} tahun - {pasien.keluhan}")
    
    def menu_utama(self):
        while True:
            print("\n=== SISTEM KLINIK ===")
            print("1. Daftarkan Pasien")
            print("2. Cari Data Pasien")
            print("3. Lihat Semua Pasien")
            print("4. Keluar")
            
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                self.tambah_pasien()
            elif pilihan == "2":
                nama = input("Masukkan nama pasien yang dicari: ")
                pasien = self.cari_pasien(nama)
                if pasien:
                    pasien.info()
                else:
                    print("Pasien tidak ditemukan!")
            elif pilihan == "3":
                self.tampilkan_semua_pasien()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan sistem klinik")
                break
            else:
                print("Pilihan tidak valid!")

klinik = Klinik()
klinik.menu_utama()