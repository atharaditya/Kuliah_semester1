import datetime 
import modul_bangun_datar

print(modul_bangun_datar.__file__)
print('Tanggal dan waktu sekarang : ', datetime.datetime.now())
print('PI:', modul_bangun_datar.PI)
print('luas persegi : ',modul_bangun_datar.luas_persegi(sisi=20))
print('luas persegi panjang : ',modul_bangun_datar.luas_persegi_panjang(panjang=15,lebar=10))
print('luas jajar genjang : ',modul_bangun_datar.luas_jajar_genjang(alas=10,tinggi=30))
print('luas segitiga : ',modul_bangun_datar.luas_segitiga(alas=5,tinggi=10))
print('luas belah ketupat : ',modul_bangun_datar.luas_belah_ketupat(d1=15,d2=20))
print('luas layang-layang : ',modul_bangun_datar.luas_layang_layang(d1=30,d2=15))
print('luas trapesium : ',modul_bangun_datar.luas_trapesium(tinggi=20,a=10,b=15))