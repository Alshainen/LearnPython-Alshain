#User Input = sebuah fungsi yang meminta pengguna untuk memasukkan data,
#             lalu mengembalikan data yang dimasukkan sebagai string.

input()
#User disuruh ngetik

nama = input('Nama kamu: ')
umur = input('Berapa umurmu: ') #Ini ga int, lu bisa ngetik selain angka
print(f'Halo {nama}! Umur kamu {umur}')
#Hasil input akan masuk ke variabel nama dan umur.


#Kita perlu konversi input ke int/float untuk umur
umurKu = int(input('Berapakah umurmu: '))

print(f'Aku {umurKu} tahun')
#User wajib memasukkan angka, jika tidak akan error.

#Kira-kira gitu lah user input, lu ngetik, hasil ketikan masuk, dan ya gitu.
#Ingat, input selalu string, maka perlu konversi tipe data dulu 
#kalau mau ganti yang lain.