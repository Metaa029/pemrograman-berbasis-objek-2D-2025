from Tunai import PembayaranTunai
from KartuKredit import PembayaranKartu
from DompetDigital import PembayaranDompet

def main():
    print("=== Sistem Pembayaran ===")
    print("Pilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. Dompet Digital")

    pilihan = input("Masukkan pilihan (1/2/3): ")
    jumlah = float(input("Masukkan jumlah pembayaran: Rp "))

    if pilihan == "1":
        metode = PembayaranTunai()
    elif pilihan == "2":
        metode = PembayaranKartu()
    elif pilihan == "3":
        metode = PembayaranDompet()
    else:
        print("Pilihan tidak valid.")
        return

    total = metode.bayar(jumlah)
    print(f"Total yang dibayar setelah diskon/biaya: Rp{total:,.2f}")

main()
