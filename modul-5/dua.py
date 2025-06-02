from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f"Tipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%\n")


class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis.")
        else:
            print(f"Laptop digunakan selama {jam} jam.")


class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        print(f"Kulkas digunakan selama {jam} jam.")


def main():
    perangkat = None

    while True:
        print("\nPilih perangkat elektronik:")
        print("1. Laptop")
        print("2. Kulkas")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            perangkat = Laptop()
        elif pilihan == "2":
            perangkat = Kulkas()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
            continue

        perangkat.nyalakan()

        while True:
            try:
                jam = int(input("Masukkan durasi penggunaan dalam jam: "))
                perangkat.gunakan(jam)
                perangkat.status()
            except ValueError:
                print("Input tidak valid. Harus berupa angka.")
                continue

            lanjut = input("Gunakan perangkat lagi? (y/n): ").lower()
            if lanjut != 'y':
                perangkat.matikan()
                break

main()
