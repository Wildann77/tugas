#permasalahan banyak orang yang masih binggun tentang selera musik yang mereka sukai 
#jadi saya membuat program untuk mengidentifikasi genre musik yang mereka sukai

nama = str(input('Masukan Nama Anda = '))
print('Pilihan Jenis Musik : keras,sedang,sangat keras, slow')
jenis_musik = str(input('Masukan Jenis Musik Yang Anda Sukai = '))
print('Pilihan Band : avenged,beach bunny,slipknot, bon jovi')
band = str(input('Masukan Band Yang Anda Sukai Atau Musisi = '))
jenis_musiklist= 'keras'
jenis_musiklist1= 'sedang'
jenis_musiklist2= 'sangat keras'
jenis_musiklist3= 'slow'
jenis_bandlist = ['avenged','beach bunny','slipknot','bon jovi']

if jenis_musik in jenis_musiklist and band in jenis_bandlist:
    print ('Genre Musik Kamu Adalah','Heavy Metal ',nama)
elif jenis_musik in jenis_musiklist1 and band in jenis_bandlist:
    print ('Genre Musik Kamu Adalah','Indie Rock ',nama)
elif jenis_musik in jenis_musiklist2 and band in jenis_bandlist:
    print ('Genre Musik Kamu Adalah','Nu Metal ',nama)
elif jenis_musik in jenis_musiklist3 and band in jenis_bandlist:
    print ('Genre Musik Kamu Adalah','Slow Rock ',nama)
    









