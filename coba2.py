class manusia:
    def __init__(self,nama,umur,pekerjaan):
        self.nama=nama
        self.umur=umur
        self.pekerjaan=pekerjaan

    def perkenalan(self):
        return (f"perkenalkan nama saya {self.nama}, saya berumur {self.umur}, dan saya bekerja sebagai {self.pekerjaan}.")
    

    @staticmethod
    def alamat():
        return "surabaya"

m1=manusia("meta",19,"HRD")
m2=manusia("farhan",18,"web developer")

print(m1.perkenalan())
print(m2.perkenalan())
print(m1.alamat())


