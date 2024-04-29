print("===============================")
print("     TOKO ES ESKRIM LOLALA     ")
print("===============================")
daftar_barang = {
    "Es Teh Anget": 100000,
    "Es Naga": 80000,
    "Es Rainbow": 20000,
    "Es Lele": 150000,
    "Es Kacang Ijo": 50000
}

print("Daftar Barang:")
for barang, harga in daftar_barang.items(): 
    print(f"{barang}: Rp {harga}")

total_belanja = 0

print("======================")


jumlah_barang = int(input("\nMasukkan jumlah barang yang dibeli: "))

daftar_belanja = []

for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
        daftar_belanja.append(barang)
    else:
        print(f"{barang} tidak ada dalam daftar barang.")

print("========================")
print("\nDaftar Barang yang Dibeli:")
for barang in daftar_belanja:
    print(barang)

print(f"\nTotal belanjaan Anda: Rp {total_belanja}")

print("============================")