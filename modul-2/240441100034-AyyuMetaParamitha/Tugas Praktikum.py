class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.cek_sks(sks) == "valid":
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print("SKS tidak valid untuk mata kuliah", nama)
            self.kode = kode
            self.nama = nama
            self.sks = 0

    @staticmethod
    def cek_sks(sks):
        if sks == 2 or sks == 3:
            return "valid"
        else:
            return "tidak valid"

    def __str__(self):
        return self.kode + " - " + self.nama + " (" + str(self.sks) + " SKS)"


class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.cek_nim(nim) == "valid":
            self.nama = nama
            self.nim = nim
        else:
            print("NIM tidak valid untuk mahasiswa", nama)
            self.nama = nama
            self.nim = "SALAH"
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa = Mahasiswa.total_mahasiswa + 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print("\nNama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("Mata Kuliah:")
        for matkul in self.matkul_diambil:
            print(" -", matkul)

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def cek_nim(nim):
        if nim.startswith("23") and len(nim) == 10:
            return "valid"
        else:
            return "tidak valid"

 
class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        cek = Kampus.cek_nama_kampus(nama)
        if cek == "tidak valid":
            print("Nama kampus tidak valid:", nama)

    @classmethod
    def tampilkan_info(cls, nama_kampus):
        print("\nKampus:", nama_kampus)
        print("Total Mahasiswa:", Mahasiswa.jumlah_mahasiswa())

    @staticmethod
    def cek_nama_kampus(nama):
        angka = "0123456789"
        for huruf in nama:
            if huruf in angka:
                return "tidak valid"
        return "valid"


matkul1 = MataKuliah("MK101", "Matematika", 3)
matkul2 = MataKuliah("MK102", "PBO", 3)
matkul3 = MataKuliah("MK103", "Struktur Data", 3)
matkul4 = MataKuliah("MK104", "Basis Data", 2)
matkul5 = MataKuliah("MK105", "Pemrograman Web", 3)
matkul6 = MataKuliah("MK106", "Sistem Operasi", 2)
matkul7 = MataKuliah("MK107", "Jaringan", 3)
matkul8 = MataKuliah("MK108", "Algoritma Pemrograman", 4)  

mhs1 = Mahasiswa("Bima", "2412345030", "Informatika")
mhs2 = Mahasiswa("Farhan", "2412345150", "Informatika")
mhs3 = Mahasiswa("Jois", "2412345112", "Sistem Informasi")
mhs4 = Mahasiswa("Arzha", "2412345064", "Informatika")
mhs5 = Mahasiswa("Irsyad", "2412345102", "Teknik Komputer")
mhs6 = Mahasiswa("Rifqi", "123456789", "Sistem Informasi")  


for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tambah_matkul(matkul1)
    mhs.tambah_matkul(matkul2)
    mhs.tambah_matkul(matkul3)
    mhs.tambah_matkul(matkul4)


kampus1 = Kampus("Universitas Teknologi", "Jl. teknologi No. 29")


print("\n===== DATA MAHASISWA =====")
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tampilkan_info()


print("\n===== DATA KAMPUS =====")
Kampus.tampilkan_info(kampus1.nama)
print("Cek nama kampus:", Kampus.cek_nama_kampus(kampus1.nama))
