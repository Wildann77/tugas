nama = str(input('Masukan Nama '))
umur = int(input('Masukan Umur '))
kerja_ortu = str(input('Masukan Pekerjaan '))
gaji = int(input('Masukan gaji '))
ipk  = float(input('Masukan Ipk '))
perkerjaan_ortu = ['serabutan','pedagang']

if kerja_ortu in perkerjaan_ortu and gaji <= 1000000 and ipk >= 2.7 and umur <= 25 :
    print("Keterima","Nama =",nama,"Umur =",umur,"Pekerjaan Orang tua =",kerja_ortu,"Gaji Orang tua =",gaji,"Ipk =",ipk)
  
else:
    print("Engga Keterima","Nama =",nama,"Umur =",umur,"Pekerjaan Orang tua =",kerja_ortu,"Gaji Orang tua =",gaji,"Ipk =",ipk)
  

