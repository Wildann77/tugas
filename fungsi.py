def sapaan():
    print('Hello World')

sapaan()
sapaan()
sapaan()

def salam(ucapan):
    print(ucapan)

salam('Selamat Siang')

def penjumlahan(a,b):
    hasil = a+b
    print(hasil)

penjumlahan(5,10)

def luas_persegi_panjang(panjang,lebar):
    return panjang*lebar
print(luas_persegi_panjang(5,8))

def nilai(a,b,c,d):
    jum1 = a +b
    jum2 = c-b
    return jum1,jum2
print(nilai(1,2,3,4))

nama = 'iwak'
def cektak():
    nama = 'ikan'
    print(nama)
cektak()