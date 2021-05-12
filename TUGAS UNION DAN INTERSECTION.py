# A = Himpunan Bilangan Genap dari 1 - 20
# B = Himpunan Bilangan Ganjil dari 1 - 20
# C = Himpunan bilangan Negatif lebih besar dari -20
# D = Himpunan Bilangan Prima dari 1 - 20
# E = Himpunan Bilangan Komposit dari 1 - 20
# Bilangan Komposit = Bukan Bilangan Prima 

# u = Union
# n = Irisan

# a. A u B u C u D u E
# b. (A n B) u (D n E)
# c. (A u B) n (D u E)
# d. (A u B) - (D u E)
# e. (A u B u C) - (A n E)

## Membuat data isi himpunan nya menggunakan Fungsi
# A = {2, 4, 6, 8, 10, 12, ...}

A = set()
B = set()
C = set()
D = set()
E = set()

for i in range(1,21) :
    if i % 2 == 0 :
        i = i
        
    else :
        continue
    A.add((i))

print('A = ', A)

for i in range(1,21) :
    if i % 2 != 0 :
        i = i
        
    else :
        continue
    B.add((i))

print('B = ', B)

for i in range(-19,0) :
    i = i
    C.add((i))

print('C = ', C)

for x in range(1,21): 
    if x > 1: 
        for i in range(2,x): 
            if (x % i) == 0: 
                break 
        else: 
            D.add((x))

print('D = ', D)

for x in range(1,21): 
    if x > 1: 
        for i in range(2,x): 
            if (x % i) == 0: 
                E.add((x))
                break
        else: 
            continue

print('E = ', E)

# u = Union |
# n = Irisan &

a = (A | B | C | D | E)
b = (A & B) | (D & E)
c = (A | B) & (D | E)
d = (A | B) - (D | E)
e = (A | B | C) - (A & E)

print('a = ', a, 'adalah (A | B | C | D | E)')
print('b = ', b, 'adalah (A & B) | (D & E)')
print('c = ', c, 'adalah (A | B) & (D | E)')
print('d = ', d, 'adalah (A | B) - (D | E)')
print('e = ', e, 'adalah (A | B | C) - (A & E)')