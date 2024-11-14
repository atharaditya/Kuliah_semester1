# program 2.5 volume dan luas permukaan bola

def bola():
    r = int(input('masukan jari-jari bola : '))
    t = int(input('masukan tinggi bola : '))

    luas = 4*3.14*r*r
    volume = float(4)/3*22/7*r*r*r

    print('luas bola : ' + str(luas))
    print('volume bola : ' + str(volume))

bola()