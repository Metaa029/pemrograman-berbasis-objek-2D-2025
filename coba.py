# modul 1 dan 2

class mahasiswa:
    jumlah_mahasiswa=0

    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
        mahasiswa.jumlah_mahasiswa += 1

    def perkenalan(self):
        return(f"nama saya {self.nama}, umur {self.umur}")
    
    @classmethod
    def total_mahasiswa(cls):
        return(f"total mahasiswa saat ini: {cls.jumlah_mahasiswa}")
    
    @staticmethod
    def info_kampus():
        return "universitas teknologi"

mahasiswa1=mahasiswa("meta",19)
mahasiswa2=mahasiswa("farhan",18)

print (mahasiswa1.perkenalan())
print (mahasiswa2.perkenalan())
print (mahasiswa.total_mahasiswa())
print (mahasiswa.info_kampus())


# modul 3
# inheritance
class mobil:
    def __init__(self,nama,roda):
        self.nama=nama
        self.roda=roda

    def bergerak(self):
        print(f"mobil {self.nama}, beroda {self.roda} melaju dengan cepat.")

    def berhenti(self):
        print(f"mobil {self.nama}, beroda {self.roda} berhenti di parkiran kampus.")
    
mobil1=mobil("pajero",4)
mobil2=mobil("crv",4)

print(mobil1.bergerak())
print(mobil2.berhenti())