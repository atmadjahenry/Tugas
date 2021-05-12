'''[Grade nilai]
Input:
- Masukkan nilai:

Kondisi:
- 90 ke atas : Grade A
- 85 ke atas : Grade A-
- 80 ke atas : Grade B
- 75 ke atas : Grade B -
- 70 ke atas : Grade C
- 65 ke atas : Grade D
- Di bawah 65 : 'Anda tidak lulus dan perlu remedial.'

Ketentuan:
- Nilai maksimum 100, nilai minimum 0
- Jika nilai di atas 100 : 'Nilai di luar jangkauan.'
- Jika nilai di bawah 0 : 'Tidak menerima nilai negatif.'
- Jika hasil input bukan angka : 'Angka yang Anda masukkan salah.'
- Bisa menerima nilai desimal.

Output:
Nilai Anda ... dan Anda ... (sesuai kondisi).'''


try:
        nilai = float(input('Masukkan nilai = '))

        if nilai > 100 : # pake antara, biar posisinya bisa berubah ubah
            grade = 'nilai di luar jangkauan'
        elif nilai > 90 :
            grade = 'A'
        elif nilai > 85 :
            grade = 'A-'
        elif nilai > 80 :
            grade = 'B'
        elif nilai > 75 :
            grade = 'B-'
        elif nilai > 70 :
            grade = 'C'
        elif nilai > 65 :
            grade = 'D'
        elif nilai < 0 :
            grade = 'tidak menerima nilai negatif'
        else :
            grade = 'Anda tidak lulus dan perlu remidial'
        print('Nilai anda {} dan anda {}'.format(nilai,grade))
        
except:
    print('Angka yang Anda masukkan salah')