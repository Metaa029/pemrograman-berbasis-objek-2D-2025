from bukuFiksi import BukuFiksi
from bukuReferensi import BukuReferensi

def main():
    print("=== Sistem Peminjaman Buku ===")
    print("Pilih jenis buku:")
    print("1. Buku Fiksi")
    print("2. Buku Referensi")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        buku = BukuFiksi()
    elif pilihan == "2":
        buku = BukuReferensi()
    else:
        print("Pilihan tidak valid.")
        return

    print("Pilih aksi:")
    print("1. Pinjam")
    print("2. Reservasi")

    aksi = input("Masukkan aksi (1/2): ")

    if aksi == "1":
        try:
            buku.pinjam()
        except AttributeError:
            print("Buku ini TIDAK dapat dipinjam.")
    elif aksi == "2":
        buku.reservasi()
    else:
        print("Pilihan aksi tidak valid.")


main()
