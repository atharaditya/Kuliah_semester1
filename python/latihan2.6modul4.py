# program 2.6 volume dan luas permukaan dan luas selimut tabung

def tabung():
    r = int(input('masukan jari-jati tabung : '))
    t = int(input('masukan tinggi tabung : '))
    d = r*2
    k = float(22)/7*d

    luas_alas = float(22)/7*(r*r)
    luas_selimut = k*t
    luas = 2*luas_alas+luas_selimut
    volume = luas_alas*t

    print('luas permukaan tabung : ' + str(luas))
    print('volume tabung : ' + str(volume))
    print('luas selimut tabung : ' + str(luas_selimut))

tabung()