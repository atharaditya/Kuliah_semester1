# program 2.4 volume dan luas permukaan dan selimut kerucut

def kerucut():
    r = int(input('masukan jari-jari kerucut : '))
    t = int(input('masukan tinggi kerucut : '))

    s = (t*t+r*r)**(float(1)/2)
    luas_selimut = float(22)/7*r*s

    luas = float(22)/7*(r*r)+luas_selimut
    volume = float(1)/3*22/7*r*r*t

    print('luas kerucut : ' + str(luas))
    print('volume kerucut : ' + str(volume))
    print('luas selimut kerucut : ' + str(luas_selimut))

kerucut()