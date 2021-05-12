'''[Mengganti Huruf vokal]
Input:
- Masukkan teks: 'Hari ini adalah hari Rabu.'
- Masukkan huruf vokal: 'o'

Output:
Horo ono odoloh horo Robo.
'''

import re


vokal = '[aeiou]' 
teks = input('Masukkan teks = ').lower()
pengganti = input('Masukkan karakter pengganti = ').lower()

output = re.sub(vokal, pengganti, teks)


print(output)