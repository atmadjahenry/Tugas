'''[Jumlah hari]
Input:
- Masukkan jumlah hari:

Output:
... tahun ... bulan ... minggu ... hari.

1 tahun = 365 hari, 1 bulan = 30 hari.'''

'''hari = int(input('Masukkan jumlah hari = '))

tahun = round(hari / 365)
tahun1 = hari % 365

bulan = round(tahun/12)
bulan1 = hari % 12

minggu = round(bulan/30)
hari = minggu % 30



print(tahun)
print(bulan)
print(minggu)
print(hari)'''
# handle kalo harinya desimal, sama harinya minus, sama huruf, keluar notifikasinya terserah


import math

jumlah_hari = int(input('Masukkan jumlah hari = '))

setahun = 365
sebulan = 30
seminggu = 7

tahun = math.floor(jumlah_hari / setahun)
sisatahun = jumlah_hari % setahun # %modulo

bulan = math.floor(sisatahun / sebulan)
sisabulan = sisatahun % sebulan

minggu = math.floor(sisabulan / seminggu)
hari = sisabulan % seminggu

if tahun < 10 :
    tahun1 = ('0' + str(tahun))
else :
    tahun1 = tahun

if bulan < 10 :
    bulan1 = ('0' + str(bulan))
else :
    bulan1 = bulan

minggu1 = ('0' + str(minggu))

hari1 = ('0' + str(hari))
   

print('{} tahun {} bulan {} minggu {} hari'.format(tahun1, bulan1, minggu1, hari1))