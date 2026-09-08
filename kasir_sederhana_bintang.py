nama_barang = "Kopi"
harga_barang = 10000

print(f"Barang: {nama_barang}")
print(f"Harga: Rp {harga_barang}")
# Data barang sudah siap

try:
    # Perbaikan: Variabel jumlah_barang dipindah ke baris baru agar tidak menyatu dengan input
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))

    total_harga = harga_barang * jumlah_barang
    print(f"Total yang harus dibayar: Rp {total_harga}")

    uang_dibayar = int(input("Masukkan uang pembayaran: "))

    # Perbaikan indentasi pada blok if-else
    if uang_dibayar < total_harga:
        print("Uang pembayaran kurang")
    else:
        kembalian = uang_dibayar - total_harga
        print(f"Uang kembalian: Rp {kembalian}")

except ValueError:
    # Perbaikan indentasi pada blok print di dalam except
    print("Error: Masukkan angka yang valid")
