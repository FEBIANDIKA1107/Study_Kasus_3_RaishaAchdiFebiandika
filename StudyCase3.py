#daftar buku 
daftar_buku = (
    "Bumi",
    "Bulan",
    "Matahari",
    "Bintang",
    "Komet",
    )

pinjaman = []

print("Daftar Buku yang Tersedia:")
for buku in daftar_buku:
    print("-", buku)

while True:
    pilihan = input("Masukkan judul buku yang ingin dipinjam (ketik 'selesai' untuk berhenti): ")

    if pilihan.lower() == "selesai":
        break

    if pilihan in daftar_buku:
        pinjaman.append(pilihan)
        print("Buku berhasil dipinjam")
    else:
        print("Buku tidak tersedia")

print("\nDaftar buku yang dipinjam:")
for buku in pinjaman:
    print("-", buku)
hapus = input("\nMasukkan buku yang ingin dihapus: ")
if hapus in pinjaman:
    pinjaman.remove(hapus)
    print("Buku berhasil dihapus")
else:
    print("Buku tidak ada dalam daftar pinjaman.")

print("\nDaftar pinjaman akhir:")
for buku in pinjaman:
    print("-", buku)
