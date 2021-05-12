# -------------------------------------------------------
# PENDEFINISIAN FUNCTION

def cekEmail(email):
    # while True:
        # email = input("Email: ")
    if email.count('@') == 1:
        splitemail = email.split('@')

        if splitemail[1].count('.') > 0:
            splitemail2 = splitemail[1].split('.')
            username = splitemail[0]
            hosting = splitemail2[0]
            ekstensi = splitemail2[1]
        
            if username.isalnum() == True or username.count('_') > 0 or username.count('.') > 0:
                if hosting.isalnum() == True:
                    if ekstensi.isalpha() == True and len(ekstensi) <= 5:
                        ket = 'Email valid'
                        # print(status)
                        # return email 
                    else:
                        ket = 'Format ekstensi yang Anda masukkan salah'
                        # print(status)  
                else:
                    ket = 'Format hosting yang Anda masukkan salah'
                    # print(status)  
            else:
                ket = 'Format username yang Anda masukkan salah'
                # print(status)  
        else:
            ket = 'Tidak ada . ekstensi, format Email Salah'
            # print(status)                  
    else:
        ket = 'Tidak ada @ atau @ lebih dari satu, format Email Salah'
        # print(status)
    return(email, ket)  

def cekPassword(password):
    # while True:
        # password = input("Password: ")
    if len(password) < 8:
        ket = "Password minimal 8 karakter"
    elif not any(i.isupper() for i in password): 
        ket = "Password harus mengandung huruf kapital"
    elif not any(i.islower() for i in password): 
        ket = "Password harus mengandung huruf kecil"        
    elif not any(i.isdigit() for i in password):
        ket = "Password harus mengandung angka"
    else:
        ket = "Password valid"
    return(password, ket)

def cekUserid(userid):
    # while True:
        # userid = input('User ID: ')
    if len(userid) < 6:
        ket = "User ID minimal 6 karakter"
    elif userid.isalnum() == True: 
        if not any(i.isalpha() for i in userid):
            ket = "User ID harus mengandung alfabet"
        elif not any(i.isdigit() for i in userid):
            ket = "User ID harus mengandung angka"
        else:
            ket = "User ID valid"
    else:
        print("User ID hanya kombinasi huruf dan angka")
    return(userid, ket)

#2
def Kalkulator():
    print()
    print('-'*9+ ' Submenu Kalkulator ' + '-'*9)

    while True:
        try:
            input1 = int(input('Masukan angka pertama: '))
            input2 = int(input('Masukan angka kedua: '))     
            operator = input('Masukan operator: ')

            if operator == '+':
                hasil = input1 + input2
                print(hasil)
                break
            elif operator == '-':
                hasil = input1 - input2
                print(hasil)
                break
            elif operator == '/':
                hasil = input1 / input2
                print(hasil)
                break
            elif operator == '*':
                hasil = input1 * input2
                print(hasil)
                break
            else:
                print('Hanya menerima operator +, -, /, *')
            
        except:
            print('Hanya menerima integer')

    while True:
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                Kalkulator()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#3
def romawi():
    DictRomInt = {"M" : 1000, "CM" : 900, "D": 500, "CD": 400, "C" : 100, "XC" : 90, "L": 50, "XL":40,"X": 10, "IX": 9, "V": 5, "IV":4, "I": 1}

    while True:
        print()
        print('Pilih:')
        print('a. Integer ke romawi')
        print('b. Romawi ke Integer')
        pilihan = input('(a/b): ')

        print()
        if pilihan == 'a' or pilihan == 'A':
            try:
                inputangka = int(input('Masukan angka: '))

                # Karena dari Dict tdk bisa langsung akses key brdskn valuenya, jadi Dict nya dibuat jadi List biar gampang        
                def int_romawi(angka):
                    hasil = ''
                    a = 0
                    rom = []
                    Int = []

                    # #Konversi Dict ke list
                    for x, y in DictRomInt.items():
                        rom.append(x)
                        Int.append(y)
                    # #print(rom)
                    # #print(Int)

                    # #Program konversi integer ke romawi
                    if angka < 4000 and angka > 0:
                        while angka > 0:
                            for i in range(angka // Int[a]):
                                hasil += rom[a]
                                angka -= Int[a]
                            a += 1                        
                    elif angka < 0:
                        hasil = 'Tidak menerima angka negatif'
                    else: 
                        hasil = 'Angka di luar jangkauan'
                    return hasil

                # Menjalankan function integer ke romawi
                print(int_romawi(inputangka))

            except:
                print('Format input salah')


        elif pilihan == 'b' or pilihan == 'B':
            def romawi_int(angka):
                i = 0
                hasil = 0

                while i < len(angka):
                    if i + 1 < len(angka) and angka[i:i+2] in DictRomInt:
                        hasil += DictRomInt[angka[i:i+2]]
                        i += 2
                    else:
                        hasil += DictRomInt[angka[i]]  
                        i += 1
                
                if hasil <= 4000:
                    return hasil
                else:
                    hasil = 'Angka melampaui batas'
                    return hasil

            inputangka = input('Masukan angka romawi: ')

            if inputangka.isalpha() == False:
                print('Harap masukan angka romawi')
            else:
                # Menjalankan function integer ke romawi
                inputangka = inputangka.upper()
                print(romawi_int(inputangka))

        else:
            print('Hanya menerima a dan b')
            continue #untuk ngeskip break di bawah

        break #untuk ngebreak while True di atas print()


    while True:
            print()
            print('1. Kembali ke MENU HOME')
            print('2. Kembali ke submenu sebelumnya')
            try:
                pilih_popup = int(input('Pilihan: '))
                if pilih_popup == 1:
                    menuHome(userid_login)
                    break
                elif pilih_popup == 2:
                    romawi()
                    break
                else:
                    print('Hanya menerima input 1 dan 2')
            except:
                print('Format input salah')

#4
def sandiMorse():
    print()
    print('-'*9+ ' Submenu Sandi Morse ' + '-'*9)
    kamus = {
    'A':'._', 'B':'_...', 'C':'_._.', 'D':'_..', 'E':'.', 
    'F':'.._.', 'G':'__.', 'H':'....', 'I':'..', 'J':'.___',
    'K':'_._', 'L':'._..', 'M':'__', 'N':'_.', 'O':'___',
    'P':'.__.', 'Q':'__._', 'R':'._.', 'S':'...', 'T':'_',
    'U':'.._', 'V':'..._', 'W':'.__', 'X':'_.._', 'Y':'_.__', 'Z':'__..', 
    '1':'.____', '2':'..___', '3':'...__', '4':'...._', '5':'.....',
    '6':'_....', '7':'__...', '8':'___..', '9':'____.', '0':'_____'
        }

    alfabet = list(kamus)
    morse   = list(kamus.values())
    word = input('Masukkan kata/kalimat : ')

    while True:
        output = ''
        word = word.upper()
        word = word.split()
        word = ''.join(word)
        for i in word:
            if i in alfabet:
                morse_1 = morse[alfabet.index(i)]
                output = output + morse_1 + ' / '
            elif i in morse:
                alfabet_1 = alfabet[morse.index(i)]
                output = output + alfabet_1
            elif i == '/':
                output = output + ' '
            else:
                output = output + i + ' / '
        print(output)
        break


    while True:
            print()
            print('1. Kembali ke MENU HOME')
            print('2. Kembali ke submenu sebelumnya')
            try:
                pilih_popup = int(input('Pilihan: '))
                if pilih_popup == 1:
                    menuHome(userid_login)
                    break
                elif pilih_popup == 2:
                    sandiMorse()
                    break
                else:
                    print('Hanya menerima input 1 dan 2')
            except:
                print('Hanya menerima integer')

#5
def hitungHari():
    print()
    print('-'*10+ ' Submenu Hitung Hari ' + '-'*10)
    hari = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']
    
    while True:
        try:
            input_hari = input("\nMasukkan nama Hari : ")
            input_hari = input_hari.lower()

            for i in hari:
                if i == input_hari:
                    jumlah = int(input('Masukkan Jumlah : '))
                    mod_jumlah = jumlah%7

                    if jumlah >= 0:
                        index_hari = hari.index(input_hari)
                        penjumlahan_hari = index_hari + mod_jumlah
                        hasil_hari = hari[penjumlahan_hari-7]
                        print(f'{jumlah} hari dari hari {input_hari} adalah hari {hasil_hari}')
                        break
                    else:
                        index_hari = hari.index(input_hari)
                        pengurangan_hari = index_hari + mod_jumlah
                        hasil_hari = hari[pengurangan_hari]
                        print(f'{jumlah} hari dari hari {input_hari} adalah hari {hasil_hari}')
                        break
                    
                elif i != input_hari and i == hari[len(hari)-1]:
                    print('Hari tidak ditemukan')
                    continue
            break
        except:
            print('Hanya menerima integer untuk Jumlah')

    while True:
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                hitungHari()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#6 
def kamusHari():
    print()
    print('-'*3+ ' Submenu Kamus Hari (Indo-Inggris) ' + '-'*3)

    hari = {"senin" : "monday",
            "selasa": "tuesday",
            "rabu": "wednesday",
            "kamis": "thursday",
            "jum'at":"friday",
            "sabtu" : "saturday",
            "minggu" : "sunday"
            }

    while True:
        input_hari = input("Masukkan Nama Hari : ")
        input_hari = input_hari.lower()

        if input_hari in hari:
            eng = hari[input_hari]
            print(f"Hari {input_hari.title()} dalam bahasa inggris adalah {eng.title()}")
            break

        else:
            print('Hari tidak ditemukan')

    while True:
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                kamusHari()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#7
def CaesarCipher():
    print()
    print('-'*9+ ' Submenu Caesar Cipher ' + '-'*9)

    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    while True:
        try:
            inputkata = str(input('Masukan kata: '))
            inputangka = int(input('Masukan angka: '))
            mod_angka = inputangka%len(alfabet)

            if inputkata.isalpha() == True:
                for i in inputkata:
                    indexi = alfabet.index(str(i))
                    jml_alfa = indexi + mod_angka
                    cc = alfabet[jml_alfa-len(alfabet)]
                    print(cc, end='')

                break

            else:
                print('Hanya bisa memasukan 1 kata')        

        except:
            print('Format input salah')
  
    while True:
        print()
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                CaesarCipher()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#8
def konversiHari():
    print()
    print('-'*9+ ' Submenu Konversi Hari ' + '-'*9)

    while True:
        try:
            jumlah_hari = int(input("Masukkan Jumlah Hari: "))

            if jumlah_hari<0:
                print("Tidak menerima angka negatif")
            else:
                tahun = 365
                bulan = 30
                minggu = 7

                x_tahun = jumlah_hari//tahun
                sisa_hari = jumlah_hari%tahun

                x_bulan = sisa_hari//bulan
                sisa_hari = sisa_hari%bulan

                x_minggu = sisa_hari//minggu
                sisa_hari = sisa_hari%minggu

                if len(str(x_tahun)) == 1:
                    if len(str(x_bulan)) == 1:
                        print(f"0{x_tahun} Tahun 0{x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")
                    else:
                        print(f"0{x_tahun} Tahun {x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")                
                else:
                    if len(str(x_bulan)) == 1:
                        print(f"{x_tahun} Tahun 0{x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")
                    else:
                        print(f"{x_tahun} Tahun {x_bulan} Bulan 0{x_minggu} Minggu {sisa_hari} Hari")
                break

        except:
            print("Angka yang Anda masukkan salah")
    
    while True:
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                konversiHari()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#9
def faktorial() :
    print()
    print('-'*9+ ' Submenu Faktorial ' + '-'*9)

    while True:
        try:
            angka = int(input('Masukkan angka = '))
            x = 1
        
            for i in range(1, angka + 1) :
                x *= i # (1*1 1*2 2*3 dsb)
            print('Hasil faktorial dari {} adalah = {}'.format(angka,x))
            break

        except:
            print('Hanya menerima integer')

    while True:
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                faktorial()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer') 

#10 fibo
def Fibonacci():
    print()
    print('-'*9+ ' Submenu Fibonacci ' + '-'*9)

    while True:
        try :
            print()
            angka = int(input('Masukkan angka = '))
            x = 0
            y = 1
            z = 0

            print('Deret Fibonacci untuk angka {} :'.format(angka))

            for i in range(angka):
                print(x, end= ' ')
                z = x + y 
                x = y
                y = z
            break

        except :
            print('Hanya menerima integer')

    while True:
        print()
        print()
        print('1. Kembali ke MENU HOME')
        print('2. Kembali ke submenu sebelumnya')
        try:
            pilih_popup = int(input('Pilihan: '))
            if pilih_popup == 1:
                menuHome(userid_login)
                break
            elif pilih_popup == 2:
                Fibonacci()
                break
            else:
                print('Hanya menerima input 1 dan 2')
        except:
            print('Hanya menerima integer')

#12 crud

def menuHome(userid):
    print()
    print("MENU HOME APLIKASI SERBA BISA")
    print("1. Data Personal (User Profile)")
    print("2. Kalkulator")
    print("3. Konversi Romawi")
    print("4. Konversi Kode Morse")
    print("5. Hitung Hari")
    print("6. Kamus Hari (Indo-Inggris)")
    print("7. Caesar Cipher")
    print("8. Konversi Jumlah Hari")
    print("9. Nilai Faktorial")
    print("10. Jumlah dan Deret Fibonacci")
    print("11. Data Akun")
    print("12. Menu CRUD")
    print("13. Exit")
    try:
        input_menu_home = int(input('Masukan pilihan menu: '))

        if input_menu_home == 1:
            printDataPersonal(userid_login)
        elif input_menu_home == 2:
            Kalkulator()
        elif input_menu_home == 3:
            romawi()
        elif input_menu_home == 4:
            sandiMorse()
        elif input_menu_home == 5:
            hitungHari()
        elif input_menu_home == 6:
            kamusHari()
        elif input_menu_home == 7:
            CaesarCipher()
        elif input_menu_home == 8:
            konversiHari()
        elif input_menu_home == 9:
            faktorial()
        elif input_menu_home == 10:
            Fibonacci()
        elif input_menu_home == 11:
            printDataUser(userid_login)
        elif input_menu_home == 12:
            print()# crud()
        elif input_menu_home == 13:
            keluar = 'Anda keluar aplikasi'
            print(keluar)
        else:
            print('Pilihan tak tersedia')

    except:
        print('Format salah')


#-------------------------------------------------------------------------------
# VARIABEL UNTUK MENJALANKAN PROGRAM

all_data_user = {}
all_data_personal = {}
keluar = ''

#-------------------------------------------------------------------------------
# MULAI PROGRAM

while keluar != 'Anda keluar aplikasi':
    print()
    print("MENU")
    print("1. Register")
    print("2. Login")

    try:
        input_menu_awal = int(input('Opsi: '))
        
        if input_menu_awal == 1: 
            # Register()
            status_uid =''
            status_pw =''
            status_e =''

            print()

            ### Register akun
            while status_uid != 'User ID valid':
                userid = input('User ID: ')

                if userid not in all_data_user:
                    hasil_uid = cekUserid(userid)
                    status_uid = hasil_uid[1]   
                    print(status_uid)
                else:
                    print('Username sudah ada')

            while status_pw != 'Password valid':
                password = input("Password: ")
                hasil_pw = cekPassword(password)
                status_pw = hasil_pw[1]
                print(status_pw)

            while status_e != 'Email valid':
                email = input("Email: ")
                hasil_e = cekEmail(email)
                status_e = hasil_e[1]
                print(status_e)

            user = [userid, password, email]
            all_data_user[user[0]] = user
            print(all_data_user)

            def printDataUser(iduser):
                if iduser in all_data_user:
                    print()
                    print('Data Akun')
                    print(f'User ID: {all_data_user[iduser][0]}')
                    print(f'Password: {all_data_user[iduser][1]}')
                    print(f'Email: {all_data_user[iduser][2]}')

                    while True:
                        print()
                        print('1. Kembali ke MENU HOME')
                        print('2. Kembali melihat Data Akun')
                        try:
                            pilih_popup = int(input('Pilihan: '))
                            if pilih_popup == 1:
                                menuHome(userid_login)
                                break
                            elif pilih_popup == 2:
                                printDataUser(userid_login)
                                break
                            else:
                                print('Hanya menerima input 1 dan 2')
                        except:
                            print('Hanya menerima integer')
                else:
                    print('Username salah')

            ### Mengisi data personal
            while True:
                data_personal = {}
                alamat = {}
                geo = {}

                print()
                print('Data Personal')
                nama = input('Nama: ')

                if all(x.isalpha() or x.isspace() for x in nama):
                    gender = input('Gender (Pria/Wanita): ')
                    gender = gender.lower()

                    if gender == 'pria' or gender == 'wanita':
                        while True:
                            try:
                                usia = int(input('Usia: '))

                                if 6 <= usia <= 120:
                                    job = input('Pekerjaan: ')

                                    if all(x.isalpha() or x.isspace() for x in job):
                                        hobi = input('Hobi (bisa lebih dari satu, pisahkan dengan koma lalu spasi -> (, )): ')
                                        hobi = hobi.split(', ')

                                        while True:
                                            try:
                                                print('Alamat')
                                                kota = input('Kota: ')
                                                kec = input('Kec: ')
                                                kel = input('Kel: ')
                                                zipcode = int(input('Zipcode: '))
                                                lat = float(input('Latitude: '))
                                                long = float(input('Longitude: '))
                                                geo['Latitude'] = lat
                                                geo['Longitude'] = long

                                                if all(x.isalpha() or x.isspace() for x in kota) and all(x.isalpha() or x.isspace() for x in kec) and all(x.isalpha() or x.isspace() for x in kel):
                                                    alamat['Kota'] = kota
                                                    alamat['Kel'] = kel
                                                    alamat['Kec'] = kec
                                                    alamat['Zipcode'] = zipcode
                                                    alamat['Geo'] = geo
                                                    data_personal['Alamat'] = alamat

                                                    while True:
                                                        hp = str(input('No. HP: '))
                                                            
                                                        if 11 <= len(hp) <= 13 and hp[0:2] == '08':
                                                            data_personal['Nama'] = nama
                                                            data_personal['Gender'] = gender
                                                            data_personal['Usia'] = usia
                                                            data_personal['Pekerjaan'] = job
                                                            data_personal['Hobi'] = hobi
                                                            data_personal['Alamat'] = alamat
                                                            data_personal['No. HP'] = hp

                                                            all_data_personal[userid] = data_personal
                                                            print(all_data_personal)

                                                            print('Anda berhasil register')

                                                            def printDataPersonal(iduser):
                                                                if iduser in all_data_personal:
                                                                    print()
                                                                    print('Data Personal User')
                                                                    print(f'Nama: {all_data_personal[iduser]["Nama"]}')
                                                                    print(f'Gender: {all_data_personal[iduser]["Gender"]}')
                                                                    print(f'Usia: {all_data_personal[iduser]["Usia"]}')
                                                                    print(f'Pekerjaan: {all_data_personal[iduser]["Pekerjaan"]}')
                                                                    print(f'Hobi: {all_data_personal[iduser]["Hobi"]}')
                                                                    print('Alamat:')
                                                                    print(f'- Kota: {all_data_personal[iduser]["Alamat"]["Kota"]}')
                                                                    print(f'- Kel: {all_data_personal[iduser]["Alamat"]["Kel"]}')
                                                                    print(f'- Kec: {all_data_personal[iduser]["Alamat"]["Kec"]}')
                                                                    print(f'- Zipcode: {all_data_personal[iduser]["Alamat"]["Zipcode"]}')
                                                                    print(f'- Geo: {all_data_personal[iduser]["Alamat"]["Geo"]}')
                                                                    print(f'No. HP: {all_data_personal[iduser]["No. HP"]}')
                                                                
                                                                    while True:
                                                                        print()
                                                                        print('1. Kembali ke MENU HOME')
                                                                        print('2. Kembali melihat Data Personal')
                                                                        try:
                                                                            pilih_popup = int(input('Pilihan: '))
                                                                            if pilih_popup == 1:
                                                                                menuHome(userid_login)
                                                                                break
                                                                            elif pilih_popup == 2:
                                                                                printDataPersonal(userid_login)
                                                                                break
                                                                            else:
                                                                                print('Hanya menerima input 1 dan 2')
                                                                        except:
                                                                            print('Hanya menerima integer')
                                                            break   # ngebreak whilenya no hp

                                                        else:
                                                            print('Format nomor HP salah')
                                                            continue
                                                        break   # ngebreak while di atas hp

                                                else:
                                                    print('Format alamat salah')
                                                    continue
                                                break       # ngebreak while di atas alamat
                                            except:
                                                print('Format data salah')
                                    else:
                                        print("Format data yang Anda masukan salah")
                                        continue
                                    break   # ngebreak while di atas usia
                                else:
                                    print("Usia minimal 6 tahun dan maksimal 120 tahun")
                                    continue
                                break       # ngebreak while di atas usia
                            except:
                                print("Hanya menerima integer")
                    else:
                        print("Hanya menerima input Pria/Wanita")
                        continue
                else:
                    print("Format data yang Anda masukan salah")
                    continue
                break           # ngebreak whilenya data personal


        elif input_menu_awal == 2:
            print()
            print('Silakan login')

            # print(all_data_user)
            status_login = ''
            batas_login_userid = 1
            batas_login_pw = 1

            while status_login != 'Anda berhasil login':
                while batas_login_userid <= 3:
                    userid_login = input("User ID: ")
                    if all_data_user == {}:
                        print('Daftar user masih kosong')
                        break # buat ngebreak while True di atas userid_login = input("User ID: ")
                    elif userid_login in all_data_user:
                        # Masuk ke input password
                        while batas_login_pw <= 3:
                            pw_login = input("Password: ")
                            if pw_login == all_data_user[userid_login][1]:
                                status_login = 'Anda berhasil login'
                                print(status_login)
                                menuHome(userid_login)
                                # keluar = 'Anda keluar aplikasi'
                                break           # ngebreak while batas_login_pw <= 3
                            else:
                                print('Password salah') 
                                batas_login_pw += 1          
                        break           # ngebreak batas_login_userid <= 3:
                    else:
                        print('User ID tidak ditemukan')
                        batas_login_userid += 1
                break # ngebreak while status_login != 'Anda berhasil login'
                     
                
                
            # break       # ngebreak whilenya MULAI APLIKASI

                    
        else:
            print('Hanya menerima inputan 1 atau 2')
    except:
        print('Hanya menerima inputan 1 atau 2')
