hari = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']
sekarang = str(input('Masukkan nama hari = ')).lower()

if sekarang.isalpha() == True :
    sekarang = sekarang

    if sekarang in hari :
        sekarang = sekarang
    
        try :
            jumlah = int(input('Masukkan jumlah penambahan hari = '))
            
            x = jumlah // len(hari)

            nanti = hari.index(sekarang) + jumlah - (x*len(hari))

            if nanti >= 7 :
                nanti -= 7

            else :
                nanti = nanti

            haribaru = hari[nanti]
            print(jumlah, 'hari dari hari', sekarang.title(), 'adalah hari', haribaru.title())
    
        except :
            print('Angka yang anda masukkan salah')
            
    else :
        print('Hari tidak ditemukkan')

else :
    print('Hari yang anda masukkan salah')