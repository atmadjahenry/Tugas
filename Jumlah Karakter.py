'''[Jumlah karakter]
Input:
- Masukkan kalimat: 'Hari ini tidAk masuk kuliAh.'
- Masukkan karakter: A

Output:
Jumlah karakter A di dalam kalimat ... sebanyak 4. (tidak case sensitive)
'''

kalimat = input("Masukkan Kalimat = ")
character = input("Karakter yang ingin dihitung = ").lower()

print(kalimat.lower().count(character))