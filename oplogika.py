a = True
b = False
print('A dan B',a and b)
print('A dan B',a or b)
print('NOT A', not a)
print('NOT B', not b)
bayar = bool(input('Apakah Sudah Bayar ? '))
absen = int(input('Masukan Absen '))
if bayar == True and absen >= 70:
    print(10*'=','Hasil',10*'=')
    print('Boleh Ikut Tes')
else :
    print('Tidak Boleh Masuk')