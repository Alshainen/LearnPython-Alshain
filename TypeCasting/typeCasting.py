#Type Casting = proses mengkonversi variabel dari satu tipe data ke 
#               tipe data lain: str(), int(), float(), bool()

nama = 'Riu'
umur = 19
uang = 19000.200
pelajar = False

print(type(nama), type(umur), type(uang), type(pelajar))
#cara liat tipe data variabel


#cara convert:
uangSatu = int(uang) #Float to Integer (angka dibelakang titik akan dihapus)
umurSatu = float(umur) #Integer to Float
umurDua = str(umur) #Hasilnya jadi string (ga keliatan sih, 
                    #                      tapi cek aja tipe datanya)
namaSatu = bool(nama) #String to Boolean (false jika string kosong)

print(uangSatu, umurSatu, umurDua, namaSatu)

#Kira-kira gitu lah, sisanya tes aja sendiri.