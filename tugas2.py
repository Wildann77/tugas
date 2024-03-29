nama = str(input('Masukan Nama : '))
jam_kerja = int(input('Masukan Jam Kerja :'))
tarif = int(input('tarif = '))
jamkerjabulan = jam_kerja *20
gajih =  jamkerjabulan * tarif
print(f'nama {nama}')
print(f'gajih {gajih:,}')