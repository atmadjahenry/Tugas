# Buat Def Function 
# Fizz Buzz 

# Input : Masukkan Angka :
# Output :
# ANgka dari input user akan menjadi range dari 1 - inputan tersebut 
# Output nya
# akan dicek seluruh angka tersebut 
# kemudian akan di print 
# angka yg habis dibagi 3 diubah menjadi Fizz 
# angka yg habis dibagi 5 diubah menjadi Buzz 
# angka yg habis dibagi 3 dan 5 menjadi FizzBuzz
# angka lain akan dicetak normal 


def FizzBuzz() :
    try :
        i = 0
        angka = int(input('Masukkan angka = '))
        for i in range(1, angka+1):
            if i % 3 == 0 and i % 5 == 0 :
                print ("FizzBuzz", end = ' ')
                continue
            if i % 3 == 0 :
                print ("Fizz", end = ' ')
                continue
            if i % 5 == 0 :
                print ("Buzz", end = ' ')
                continue
            else :
                print (i, end = ' ')
    
    except :
        print ('Hanya menerima integer')

FizzBuzz()