from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass


class Joko(Manusia):
    def berbicara(self):
        print("Joko berbicara dengan logat Jawa yang halus.")

    def bekerja(self):
        print("Joko bekerja sebagai petani di sawah.")

    def makan(self):
        print("Joko makan dengan tangan dan suka lalapan.")


class Beni(Manusia):
    def berbicara(self):
        print("Beni berbicara dengan cepat dan penuh semangat.")

    def bekerja(self):
        print("Beni bekerja sebagai programmer di startup.")

    def makan(self):
        print("Beni suka makan sambil menonton anime.")


class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara dengan lembut dan sopan.")

    def bekerja(self):
        print("Fani bekerja sebagai desainer grafis.")

    def makan(self):
        print("Fani suka makan makanan sehat dan bergizi.")


class Jani(Manusia):
    def berbicara(self):
        print("Jani berbicara dengan suara lantang dan tegas.")

    def bekerja(self):
        print("Jani bekerja sebagai guru matematika.")

    def makan(self):
        print("Jani makan dengan sangat teratur dan disiplin.")


def buat_karakter(nama):
    nama = nama.lower()
    if nama == "joko":
        return Joko()
    elif nama == "beni":
        return Beni()
    elif nama == "fani":
        return Fani()
    elif nama == "jani":
        return Jani()
    else:
        print("Karakter tidak dikenali.")
        return None


nama_input = input("Masukkan nama karakter (Joko, Beni, Fani, Jani): ")
karakter = buat_karakter(nama_input)

if karakter:
    print("\n=== Kegiatan Karakter ===")
    karakter.berbicara()
    karakter.bekerja()
    karakter.makan()
else:
    print("Program dihentikan karena karakter tidak valid.")
