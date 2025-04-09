class Mahasiswa:
    def __init__(self, nama, nim, fakultas, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.prodi = prodi
        self.alamat = alamat

    def infoMahasiswa(self):
        print(f"Nama       : {self.nama}")
        print(f"NIM        : {self.nim}")
        print(f"Fakultas   : {self.fakultas}")
        print(f"Prodi      : {self.prodi}")
        print(f"Alamat     : {self.alamat}")
        print("=" * 30)


jumlah_mahasiswa = int(input("Berapa banyak mahasiswa yang ingin Anda masukkan? "))
mahasiswa_list = []

for i in range(jumlah_mahasiswa):
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    fakultas = input("Fakultas: ")
    prodi = input("Prodi: ")
    alamat = input("Alamat: ")

    mahasiswa = Mahasiswa(nama, nim, fakultas, prodi, alamat)
    mahasiswa_list.append(mahasiswa)

print("\nInformasi Mahasiswa:")
for mhs in mahasiswa_list:
    mhs.infoMahasiswa()


