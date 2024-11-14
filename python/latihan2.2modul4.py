# program 2.2 volume dan luas permukaan limas segiempat

def limas_segiempat ():
    s = int(input('masukan sisi : '))
    t =int(input('masukan tinggi : '))

    sisi_miring = ((s*0.5)*(s*0.5)+(t+t))
    segi_tiga = 0.5*s*sisi_miring

    hasil_luas = (s*s)+(4*segi_tiga)
    hasil_volume = (1/3)*(s*s)*t

    print('luas limas = ',(hasil_luas))
    print('volume limas = ',(hasil_volume))

limas_segiempat()
  