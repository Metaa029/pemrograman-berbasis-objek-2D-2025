class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo=0):
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo
    
    @property
    def no_rekening(self):
        return self.__no_rekening
    
    @property
    def nama_pemilik(self):
        return self.__nama_pemilik
    
    @property
    def saldo(self):
        return self.__saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor berhasil. Saldo baru: Rp{self.__saldo:,}")
            return True
        print("Jumlah setor harus lebih dari 0")
        return False
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik berhasil. Saldo baru: Rp{self.__saldo:,}")
            return True
        print("Jumlah tarik tidak valid atau saldo tidak mencukupi")
        return False
    
    def info(self):
        print("\nInformasi Rekening:")
        print(f"No Rek: {self.__no_rekening}")
        print(f"Pemilik: {self.__nama_pemilik}")
        print(f"Saldo: Rp{self.__saldo:,}")
        print("-" * 30)

class Bank:
    def __init__(self):
        self.__daftar_rekening = []
    
    def tambah_rekening(self):
        print("\nTambah Rekening Baru")
        no_rek = input("Masukkan no rekening: ")
        nama = input("Masukkan nama pemilik: ")
        saldo_awal = float(input("Masukkan saldo awal: "))
        
        if self.cari_rekening(no_rek):
            print("No rekening sudah ada!")
            return
        
        rek_baru = RekeningBank(no_rek, nama, saldo_awal)
        self.__daftar_rekening.append(rek_baru)
        print("Rekening berhasil ditambahkan!")
    
    def cari_rekening(self, no_rekening):
        for rek in self.__daftar_rekening:
            if rek.no_rekening == no_rekening:
                return rek
        return None
    
    def transaksi(self):
        print("\nMenu Transaksi")
        no_rek = input("Masukkan no rekening: ")
        rek = self.cari_rekening(no_rek)
        
        if not rek:
            print("Rekening tidak ditemukan!")
            return
        
        while True:
            print("\n1. Setor Tunai")
            print("2. Tarik Tunai")
            print("3. Kembali")
            pilihan = input("Pilih transaksi: ")
            
            if pilihan == "1":
                jumlah = float(input("Masukkan jumlah setor: "))
                rek.setor(jumlah)
            elif pilihan == "2":
                jumlah = float(input("Masukkan jumlah tarik: "))
                rek.tarik(jumlah)
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid!")
    
    def tampilkan_semua_rekening(self):
        if not self.__daftar_rekening:
            print("\nBelum ada rekening terdaftar")
            return
        
        print("\nDaftar Rekening:")
        for i, rek in enumerate(self.__daftar_rekening, 1):
            print(f"{i}. {rek.no_rekening} - {rek.nama_pemilik} - Rp{rek.saldo:,}")
    
    def menu_utama(self):
        while True:
            print("\n=== SISTEM BANK ===")
            print("1. Tambah Rekening")
            print("2. Lakukan Transaksi")
            print("3. Lihat Daftar Rekening")
            print("4. Keluar")
            
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                self.tambah_rekening()
            elif pilihan == "2":
                self.transaksi()
            elif pilihan == "3":
                self.tampilkan_semua_rekening()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan sistem bank")
                break
            else:
                print("Pilihan tidak valid!")

bank = Bank()
bank.menu_utama()