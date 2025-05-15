class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman
    
    @property
    def judul(self):
        return self.__judul
    
    @property
    def penulis(self):
        return self.__penulis
    
    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman
    
    def info(self):
        print(f"\nJudul: {self.__judul}")
        print(f"Penulis: {self.__penulis}")
        print(f"Jumlah Halaman: {self.__jumlah_halaman}")
        print("-" * 30)

class Perpustakaan:
    def __init__(self):
        self.__katalog_buku = []
    
    def tambah_buku(self):
        print("\nTambah Buku Baru")
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        try:
            halaman = int(input("Masukkan jumlah halaman: "))
            if halaman <= 0:
                print("Jumlah halaman harus lebih dari 0")
                return
        except ValueError:
            print("Jumlah halaman harus angka")
            return
        
        buku_baru = Buku(judul, penulis, halaman)
        self.__katalog_buku.append(buku_baru)
        print("Buku berhasil ditambahkan!")
    
    def cari_buku(self, judul):
        for buku in self.__katalog_buku:
            if buku.judul == judul:
                return buku
        return None
    
    def tampilkan_semua_buku(self):
        if not self.__katalog_buku:
            print("\nBelum ada buku dalam katalog")
            return
        
        print("\nDaftar Buku:")
        for i, buku in enumerate(self.__katalog_buku, 1):
            print(f"{i}. {buku.judul} - {buku.penulis} ({buku.jumlah_halaman} halaman)")
    
    def menu_utama(self):
        while True:
            print("\n=== SISTEM PERPUSTAKAAN ===")
            print("1. Tambah Buku")
            print("2. Cari Buku")
            print("3. Lihat Katalog")
            print("4. Keluar")
            
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                self.tambah_buku()
            elif pilihan == "2":
                judul = input("Masukkan judul buku yang dicari: ")
                buku = self.cari_buku(judul)
                if buku:
                    buku.info()
                else:
                    print("Buku tidak ditemukan!")
            elif pilihan == "3":
                self.tampilkan_semua_buku()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan sistem perpustakaan")
                break
            else:
                print("Pilihan tidak valid!")

perpus = Perpustakaan()
perpus.menu_utama()