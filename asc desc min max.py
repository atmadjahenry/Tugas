# Buat Algoritma
# Buat List (Masukkan List inputan dari user)
# -- Angka - Alfa
# -- Numerik 
# Pilihan :
# 1. Ascending
# 2. Descending
# 3. Min - Max
# Output sesuai pilihan 
# 1. Angka akan di sort dari terkecil ke terbesar
# 2. Angka akan di sort dari terbesar ke terkcecil
# 3. Nilai Minimum dan Nilai Maximum

# Tidak boleh menggunakan Fungsi Sort atau [::-1] atau min() atau max()
# gunakan algoritma 

try :
    a = list(map(int,input('Masukkan angka = ').split()))




# ascending
    for i in range(len(a) - 1) :
        min_idx = i
        for j in range(i + 1, len(a)) :
            if a[min_idx] > a[j] :
                min_idx = j
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

    print(a)


# descending
    for i in range(len(a) - 1) :
        min_idx = i
        for j in range(i + 1, len(a)) :
            if a[min_idx] < a[j] :
                min_idx = j
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

    print(a)


    for i in range(len(a) - 1) :
        min_idx = i
        for j in range(i + 1, len(a)) :
            if a[min_idx] < a[j] :
                min_idx = j
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

# min
    print(a[len(a)-1])
# max
    print(a[0])

except :
    print('Hanya menerima integer')