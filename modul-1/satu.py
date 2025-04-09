class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."

manusia1 = Manusia("Farhan", 25, "Jl. Raya No. 10")
manusia2 = Manusia("Bima", 26, "Jl. Merdeka No. 5")
manusia3 = Manusia("Jois", 25, "Jl. Pattimura No. 2")
manusia4 = Manusia("Arzha", 24, "Jl. darmawangsa No. 8")
manusia5 = Manusia("Irsyad", 28, "Jl. Pahlawan No. 3")

print(manusia1.berjalan())
print(manusia2.berlari())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berjalan())
