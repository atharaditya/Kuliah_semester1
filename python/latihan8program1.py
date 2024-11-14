import random 
from random import randint

list = ['jempol', 'telunjuk', 'kelingking']
komputer = list[randint(0,2)]
pemain = False
komputer = random.choice(list)

while pemain == False:
    pemain = input('jempol, telunjuk, kelingking ? : ').capitalize()

    if pemain.lower() == komputer:
        print('seri')

    elif pemain.lower() == 'jempol' and komputer == 'kelingking':
        print('kamu kalah')

    elif pemain.lower() == 'telunjuk' and komputer == 'jempol':
        print('kamu kalah')
    
    elif pemain.lower() == 'kelingking' and komputer == 'telunjuk':
        print('kamu kalah')

    else:
        print(f'seri')

    pemain = False
    komputer = list[randint(0,2)]