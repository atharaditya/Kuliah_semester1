# program 2.3 volume dan luas permukaan balok

def balok ():
    p = int(input('masukan panjang : '))
    l = int(input('masukan lebar : '))
    t = int(input('masukan tinggi : '))

    luas = 2*(p*l*t*l*t)
    volume = p*l*t

    print('luas balok = ' + str(luas))
    print('volume balok = ' + str(volume))

balok()