def cc() :
    abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','abjad']
    try :

        a = input("Masukkan Kata = ")
        b = ""
        c = int(input("Masukkan Kunci = "))

        for x in range(len(a)):
            p = abjad.index(a[x]) + c
            b = b + abjad[p%26]

        for y in "" + b:
            print(y, end = '')

    except :
        print('Format yang anda masukkan salah')

cc()