print("Selamat Datang Di Resto Garuda Jaya")
print("===================================")
print()
resto = str(input("Resto : "))
print("Nama Resto :", resto)
alamat_resto = str(input("Alamat :"))
print("Alamat :", alamat_resto)
pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)
nomor_meja = int(input("Nomor Meja: "))
print("Nomor Meja :", nomor_meja)
tanggal_transaksi = str(input('Tanggal transaksi: '))
print("Tanggal :", tanggal_transaksi)
waktu_transaksi = str(input('Waktu transaksi : jam '))
print("Waktu :", waktu_transaksi)

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Bakso - Rp 12000")
   print("3. Mie Ayam - Rp 13000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*12000
       print (porsi," porsi Bakso = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*13000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 3000")
   print("2. Es jeruk - Rp 5000")
   print("3. kopi - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*3000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*5000
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("===================================")
print ("Nama Resto\t\t:",resto)
print ("Alamat\t\t:",alamat_resto)
print ("Nama\t\t:",pembeli)
print ("Nomor Meja\t:",nomor_meja)
print ("Tanggal\t\t:",tanggal_transaksi)
print ("Waktu\t\t:",waktu_transaksi)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")