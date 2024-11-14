import os
os.system('cls')

def segitiga(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        print()

        for j in range(i+1):
            print('*',end=' ')

    for i in range(n):
        for j in range(n+1):
            print(' ',end='')
        print()

        for j in range(n-i-1):
            print('*',end=' ')

n = int(input('masukan jumlah baris : '))
segitiga(n)