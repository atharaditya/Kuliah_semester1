# program 2.1 volume dan luas permukaan kubus

    s = float(input('masukan sisi: '))
    ls = float(input('masukan luas sisi tegak: '))
    t = float(input('masukan tinggi:'))
    luas = s**2+4*ls
    volume = 1/3*s**2*t
    print('luas: ',luas)
    print('volume: ',volume)