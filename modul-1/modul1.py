#01
class Manusia :
    nama = "Meta"
    umur = "19"

    def Menolong(self):
        print(self.nama, "menolong orang")
    pass 

manusia1 = Manusia()
print(manusia1.nama)
print(manusia1.umur)

#02
class Manusia :
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        pass

    def Menolong(self):
        print(self.nama, "menolong orang")
    pass 

manusia1 = Manusia(19, "Meta")
print("nama saya :", manusia1.nama)
print("umur saya :", manusia1.umur)


#03
class Manusia :
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        pass

    def Menolong(self):
        print(self.nama, "menolong orang")
    pass 


#04
class Mahasiswa :
    def __init__(self,namaParam,nimParam,fakultasParam,prodiParam,alamatParam):
        self.nama = namaParam
        self.nim = nimParam
        self.fakultas = fakultasParam
        self.prodi = prodiParam
        self.alamat = alamatParam

    def infoMahasiswa(self):
        print("nama :", self.nama)
        print("nim :", self.nim)
        print("fakultas :", self.fakultas)
        print("prodi :", self.prodi)
        print("alamat :", self.alamat)
        pass

mhs1 = Mahasiswa("Meta", 24034,"Teknik", "Sistem Informasi", "Bojonegoro")
mhs2 = Mahasiswa("Firda", 23110, "Teknik", "Teknik Informatika", "Gresik")
mhs3 = Mahasiswa("Farhan", 24150, "Pendidikan", "PGSD", "Tulungagung")
mhs4 = Mahasiswa("Bima", 24030, "Keislaman", "Ekonomi Syariah", "Sidoarjo")
mhs5 = Mahasiswa("Jois", 24114, "Hukum", "Ilmu Hukum", "Gresik")
mhs6 = Mahasiswa("Arzha", 24062, "Kedokteran", "Ilmu Gizi", "Sidoarjo")
mhs7 = Mahasiswa("Irsyad", 24102, "Pendidikan", "PGPAUD", "Lamongan")
mhs8 = Mahasiswa("Rifqi", 24128, "Teknik", "Teknik Sipil", "Lamongan")

mhs1.infoMahasiswa()
mhs2.infoMahasiswa()
mhs3.infoMahasiswa()
mhs4.infoMahasiswa()
mhs5.infoMahasiswa()
mhs6.infoMahasiswa()
mhs7.infoMahasiswa()
mhs8.infoMahasiswa()
