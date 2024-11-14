import datetime
import math
from Luas.segitiga import luas_segitiga
from Luas import lingkaran, persegi
from Volume.kubus import volume_kubus
from Volume.balok import volume_balok
import Luas
import Volume

print(Luas.__file__)
print(Volume.__file__)
print('Tanggal dan waktu sekarang : ',datetime.datetime.now())
print()
print('PI : ',math.pi)
print('luas segitiga : ',luas_segitiga(alas=5,tinggi=10))
print('luas lingkaran : ',lingkaran.luas_lingkaran(radius=10))
print('luas persegi : ',persegi.luas_persegi(sisi=7))
print('volume kubus : ',volume_kubus(rusuk=8))
print('volume balok : ',volume_balok(panjang=8,lebar=10,tinggi=5))