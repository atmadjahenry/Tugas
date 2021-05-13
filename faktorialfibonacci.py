def faktorial() :
    try :
        x = 1
        angka = int(input('Masukkan angka = '))
        if angka < 0:
            hasil = 'Angka yang anda masukkan harus positif'
        else :
            for i in range(1, angka + 1) :
                x *= i # (1*1 1*2 2*3 dsb)
            hasil = 'Hasil faktorial dari {} adalah = {}'.format(angka,x)
        return hasil

    except :
        hasil = 'Hanya menerima integer'


print(faktorial())


# FIBONACCI
# try :
#     angka = int(input('Masukkan angka = '))
#     x = 0
#     y = 1
#     z = 0

#     print('Deret Fibonacci untuk angka {} :'.format(angka))

#     for i in range(angka):
#         print(x, end= ' ')
#         z = x + y 
#         x = y
#         y = z

# except :
#     print('Hanya menerima integer')

# iterasi 1 =                         iterasi 4 =
# i = 0                               i = 3
# x = 0                               z = 3
#                                     x = 2
# iterasi 2 =                         y = 3
# i = 1
# z = 1                               iterasi 5 =
# x = 1                               i = 4
# y = 1                               z = 5
#                                     x = 3
# iterasi 3 =                         y = 5
# i = 2
# z = 2                               iterasi 6 =
# x = 1                               i = 5
# y = 2                               z = 8
#                                     x = 5
#                                     y = 8

# def fibonacci() :
#     x = 0
#     y = 1
#     z = 0
#     try :
#         angka = int(input('Masukkan angka = '))
    
#         hasil = 'Deret Fibonacci untuk angka {} :'.format(angka)

#         for i in range(angka):
#             x = list[x]
#             hasil = 
#             z = x + y 
#             x = y
#             y = z
#     except :
#         hasil = 'Hanya menerima input integer'
    
#     return hasil

# print(fibonacci())