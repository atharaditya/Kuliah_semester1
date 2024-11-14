PI = 22/7

def luas_kubus (sisi):
    return 6 * sisi * sisi
def keliling_kubus (rusuk):
    return 12 * rusuk

def luas_balok (panjang,lebar,tinggi):
    return 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
def keliling_balok (panjang,lebar,tinggi):
    return 4 * (panjang+lebar+tinggi)

def luas_limas_segiempat (luas_alas,luas_sisi_tegak):
    return luas_alas + luas_sisi_tegak
def volume_limas_segiempat (luas_alas,tinggi):
    return 1/3 * luas_alas * tinggi

def luas_limas_segitiga (luas_alas,luas_selubung):
    return luas_alas + luas_selubung
def volume_limas_segitiga (luas_alas,tinggi):
    return 1/3 * luas_alas * tinggi

def luas_prisma (luas_alas,luas_tutup,luas_selimut):
    return luas_alas + luas_tutup + luas_selimut
def volume_prisma (luas_alas,tinggi):
    return luas_alas * tinggi

def luas_tabung (luas_alas,luas_selimut_tabung):
    return 2 * luas_alas * luas_selimut_tabung
def volume_tabung (radius,tinggi):
    return PI * radius * tinggi

def luas_kerucut (luas_alas,luas_selimut):
    return luas_alas + luas_selimut
def volume_kerucut (radius,tinggi):
    return 1/3 * PI * radius * radius * tinggi

def luas_bola (radius):
    return 4 * PI * radius * radius
def volume_bola (radius):
    return 4/3 * PI * radius * radius * radius