kalimat = (input('Masukkan kalimat = ')).lower()
kebalik = kalimat[::-1]

if kalimat.isdigit() == True :
    print('Ini bukan termasuk kata')

elif kalimat == kebalik :
    print('Kata', kalimat, 'termasuk palindrome')
else :
    print('Kata', kalimat, 'tidak termasuk palindrome')