def jumlah(a,b):
    return a+b
def kurang(a,b):
    return a-b
def bagi(a,b):
    return a/b
def kali(a,b):
    return a*b

def operasi():
    while True:
        print('1 Penjumlahan')
        print('2 Pengurangan')
        print('3 Perkalian')
        print('4 mandeg')
        main = input('Masukan Nomor ')
        if main == '1':
            a = int(input('Masukan nomor pertama '))
            b = int(input('Masukan nomor kedua '))
            print(jumlah(a,b))
        elif main == '2':
            a = int(input('Masukan nomor pertama '))
            b = int(input('Masukan nomor kedua '))
            print(kurang(a,b))
        elif main == '3':
            a = int(input('Masukan nomor pertama '))
            b = int(input('Masukan nomor kedua '))
            print(kali(a,b))
        elif main == '4':
             break
        elif main not in ('1','2','3'):
            print('Nomor tidak valid')
            
operasi()

