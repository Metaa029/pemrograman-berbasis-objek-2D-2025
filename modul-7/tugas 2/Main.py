from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("=== Sistem Pemesanan Kendaraan ===")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")

    pilihan = input("Pilih kendaraan (1/2/3): ")
    usia = int(input("Masukkan usia Anda: "))

    if pilihan == "1":
        kendaraan = Mobil()
    elif pilihan == "2":
        kendaraan = Motor()
    elif pilihan == "3":
        kendaraan = Sepeda()
    else:
        print("Pilihan tidak valid.")
        return

    if kendaraan.pesan(usia):
        biaya = kendaraan.hitung_biaya()
        asuransi = kendaraan.biaya_asuransi()
        total = biaya + asuransi
        print(f"Biaya sewa: Rp{biaya:,.2f}")
        print(f"Asuransi: Rp{asuransi:,.2f}")
        print(f"Total bayar: Rp{total:,.2f}")

main()
