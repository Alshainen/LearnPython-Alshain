# Tantangan 1: Program Kasir

# Halo, saya pemilik toko kelontong. 
# Saya butuh program kasir sederhana yang jalan di terminal.

# Kasir mengetik tiga hal: harga satuan barang (rupiah), 
# jumlah yang dibeli, dan apakah pembeli member (kasir selalu mengetik ya atau tidak, 
# huruf kecil). Harga satuan selalu kelipatan 1.000 dan jumlah selalu bilangan bulat, 
# jadi diskon tidak akan pernah menghasilkan pecahan.

# Aturan toko:

# Member: diskon 10% kalau subtotal minimal Rp100.000, selain itu 5%.
# Bukan member: diskon 5% kalau subtotal minimal Rp100.000, selain itu tidak ada diskon.
# Ongkir Rp15.000. Gratis kalau total setelah diskon minimal Rp150.000, 
# atau kalau pembeli adalah member yang membeli minimal 10 barang.

# Program menampilkan empat baris: subtotal, diskon, ongkir, dan total bayar. 
# Semua angka ditulis polos tanpa titik ribuan, dan berupa bilangan bulat (bukan 15000.0). 
# Contoh tampilan untuk harga 25000, jumlah 4, member ya:

# Subtotal: Rp100000
# Diskon  : Rp10000
# Ongkir  : Rp15000
# Total   : Rp105000

member = True

subtotal = 0
total = 0
diskon = 0

ongkir = 15000
kenaOngkir = 0

hargaBarang = int(input("Harga satuan barang: "))
jumlahBarang = int(input("Jumlah yang dibeli: "))
adalahMember = input("Apakah kamu member? (ya/tidak): ")
if adalahMember == "ya":
    member = True
else:
    member = False
    

subtotal = hargaBarang * jumlahBarang
if member and subtotal >= 100000:
    diskon = subtotal * 10 / 100
elif (member and subtotal < 100000) or (not member and subtotal >= 100000):
    diskon = subtotal * 5 / 100
    
total = subtotal - diskon
    
if (member and jumlahBarang >= 10) or (total >= 150000):
    kenaOngkir = 0
else:
    total += ongkir
    kenaOngkir += ongkir
    
print(f"Subtotal: Rp{int(subtotal)}")
print(f"Diskon  : Rp{int(diskon)}")
print(f"Ongkir  : Rp{int(kenaOngkir)}")
print(f"Total   : Rp{int(total)}")