import datetime
from modul_bangun_ruang import luas_balok,keliling_balok
import modul_bangun_ruang

print(modul_bangun_ruang.__file__)
print('Tanggal dan waktu sekarang : ',datetime.datetime.now())
print()
print('luas balok : ',luas_balok(panjang=20,lebar=12,tinggi=10))
print('keliling balok : ',keliling_balok(panjang=20,lebar=12,tinggi=10))