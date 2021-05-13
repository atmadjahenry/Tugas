# Buat Return Function 

# # kalkulator

def kalkulator() :
    try :

        angka1 = int(input('Masukkan angka pertama = '))
        angka2 = int(input('Masukkan angka kedua = '))
        operator = input('Masukkan operatornya = ')

        if operator == '+' :
            hasilnya = (angka1 + angka2)
            hasil = ('{} {} {} = {}'.format(angka1, operator, angka2, hasilnya))
        elif operator == '-' :
            hasilnya = angka1 - angka2
            hasil = ('{} {} {} = {}'.format(angka1, operator, angka2, hasilnya))
        elif operator == '*' :
            hasilnya = angka1 * angka2
            hasil = ('{} {} {} = {}'.format(angka1, operator, angka2, hasilnya))
        elif operator == '/' :
            hasilnya = angka1 / angka2
            hasil = ('{} {} {} = {}'.format(angka1, operator, angka2, hasilnya))
        elif operator == '**' :
            hasilnya = angka1 ** angka2
            hasil = ('{} {} {} = {}'.format(angka1, operator, angka2, hasilnya))
        else :
            hasil = 'operator yang anda masukkan salah'  
    except :
        hasil = 'hanya menerima angka'

    return hasil

print(kalkulator())