### Latihan
'''
Auto - Translator

Input :
Masukkan Nama Hari : 

Kondisi :
- Tidak Case Sensitif 
- Tidak menerima inputan bukan hari, integer, float, dll

Keluar Notif : Nama Hari yg anda masukkan salah 

Output :
Tergantung Inputan 
- Jika Inputan Hari dalam bahasa Indo 
==> (f"Hari {hari} dalam bahasa inggris adalah {eng}")

- Jika Inputan Hari dalam bahasa Inggris 
==> (f"{hari} in bahasa is {indo}")
'''

### Kamus Hari
Hari = {"senin" : "monday",
        "selasa": "tuesday",
        "rabu": "wednesday",
        "kamis": "thursday",
        "jum'at":"friday",
        "sabtu" : "saturday",
        "minggu" : "sunday"}

def translator() :

    try :
        hari = str(input('Masukkan nama hari = ')).lower()

        keys = list(Hari.keys())
        values = list(Hari.values())

        # print(keys)
        # print(values)

        if hari in keys :
            english = Hari[hari]
            print('Hari', hari.title(), 'dalam bahasa Inggris adalah', english.title())
    
        else :
            indonesian = keys[values.index(hari)]
            print(hari.title(), 'in bahasa is', indonesian.title())

    except :
        print('Nama hari yang anda masukkan salah')

translator()

