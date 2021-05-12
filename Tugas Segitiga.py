# SOAL 1
print("-"*20+"SOAL 1"+"-"*20)

angka = 1
while angka < 6 :
    print((str(angka) + " ") * angka)
    angka += 1


# SOAL 2
print("-"*20+"SOAL 2"+"-"*20)

baris = 5
angka = 1
for x in range(angka, baris + angka):
    for y in range(angka, x + angka):
        print(y, end = " ")
    print()


# SOAL 3
print("-"*20+"SOAL 3"+"-"*20)

baris = 5
angka = 1
for x in range(baris, 0, -angka):
    for y in range(baris, x - angka, -angka):
        print(y, end = " ")
    print()


# SOAL 4
print("-"*20+"SOAL 4"+"-"*20)

angka = 1
batas = 6
while angka < batas:
    print((str(angka) + " ") * (batas - angka))
    angka += 1


# SOAL 5
print("-"*20+"SOAL 5"+"-"*20)

baris = 5
angka = 1
for x in range(baris, 0, -angka):
    for y in range(angka, x + angka):
        print(y, end = " ")  
    print()


# SOAL 6
print("-"*20+"SOAL 6"+"-"*20)

baris = 5
angka = 1
for x in range(baris, 0, -angka):
    for y in range(baris, baris - x, -angka):
        print(y, end = " ")
    print()


# SOAL 7
print("-"*20+"SOAL 7"+"-"*20)

baris = 10
for i in range(baris):
    if i%2 == 0:
        continue
    print(" "*(baris-i-1)+" *"*(i))   
for j in range(baris, 0, -1):
    if j%2 == 0: 
        continue
    print(" "*(baris-j-1)+" *"*(j))