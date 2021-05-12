'''[Hitung BMI (Body Mass Index)]
Rumus BMI : massa(kg) / (tinggi(m) ** 2)

Input:
- Masukkan tinggi badan (dalam cm)
- Masukkan berat badan (dalam kg)

Ketentuan: (dihandle duluan)
- Nilai tinggi dan massa tidak boleh negatif 
Keluar notif : 'Tidak menerima angka negatif.'
- Nilai tinggi dan massa tidak boleh string atau desimal (harus integer)
Keluar notif : 'Angka yang Anda masukkan salah.'
- Batas maksimal berat badan 200 kg dan batas maksimal tinggi badan 300 cm
Keluar notif : 'Tinggi/ berat badan yang Anda masukkan di luar batas.'

Kategori BMI: (baru masuk ke sini)
BMI < 18.5 : 'Berat badan kurang.'
BMI 18.5 - 24.9 : 'Berat badan ideal.'
BMI 25 - 29.9 : 'Berat badan berlebih.'
BMI 30 - 39.9 : 'Berat badan sangat berlebih.'
BMI >= 40 : 'Obesitas.'

Output:
Tinggi badan Anda ... m dan berat badan Anda ... kg, BMI Anda ... (nilai BMI) dan Anda termasuk ... (kategori BMI).
'''

try :
    tinggi = int(input('Masukkan tinggi badan = '))
    massa = int(input('Masukkan berat badan = '))
    
    tinggim = tinggi / 100
    if tinggi > 300 :
        print('Tinggi/berat yang anda masukkan di luar batas')
    elif massa > 200 :
        print('Tinggi/berat yang anda masukkan di luar batas')
    elif tinggi < 0 :
        print('Tidak menerima angka negatif')
    elif massa < 0 :
        print('Tidak menerima angka negatif')
    else :

        bmi = float(massa / (tinggim ** 2))

        if bmi < 18.5 :
            kategori = 'berat badan kurang'
        elif bmi < 25 :
            kategori = 'berat badan ideal'
        elif bmi < 30 :
            kategori = 'berat badan berlebih'
        elif bmi < 40 :
            kategori = 'berat badan sangat berlebih '
        else :
            kategori = 'obesitas'   
        print(f'Tinggi badan anda {tinggim} m dan berat badan anda {massa} kg, BMI anda' , round(bmi,1) , f'dan anda termasuk {kategori}.')
except:
    print('Angka yang Anda masukkan salah')