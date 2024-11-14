key = int(input('Masukan berapa langkah :'))
message = str(input('String yang di enskrip :'))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
hasil = ''

for i in message:
    if i in alphabet:
        num = alphabet.find(i)
        if key <= 1:
            num += key
        elif key >= 2:
            num -= key
        if num >= len(alphabet):
            num -= len(alphabet)
        elif num < 0:
            num += len(alphabet)
        hasil += alphabet[num]
    else:
        hasil += i
print('pesan yang di deskrip :',hasil)