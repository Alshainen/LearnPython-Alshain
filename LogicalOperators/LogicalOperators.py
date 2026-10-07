# Logical Operators = Kondisi ganda di if statements
#                     or = salah satunya harus sesuai kondisi
#                     and = keduanya harus sesuai kondisi
#                     not = membalikkan kondisi (tidak true / tidak false)


age = 29
isStudent = True

if age < 30 and isStudent == False:
    print("Kau sebaiknya sekolah")
elif age >= 30 and isStudent == True:
    print("Umur se-gini masih sekolah?")
elif age >=30 and isStudent == False:
    print("Kerja apa lu?")
elif age < 30 and isStudent == True:
    print("Sekolah di mana lu?")

# or = salah satu kondisi harus True
if age < 18 or isStudent:
    print("Kamu dapat diskon pelajar atau anak-anak")
else:
    print("Kamu tidak mendapat diskon")

# not = membalikkan nilai True menjadi False, dan sebaliknya
if not isStudent:
    print("Kamu bukan pelajar")
else:
    print("Kamu pelajar")
