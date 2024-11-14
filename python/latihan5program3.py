# program 3 mengecek usia

usia = int(input('masukan umur : '))
print()

if usia<=5 :
    print('status anda masih balita')
elif usia<=12 :
    print('status anda masih anak=anak')
elif usia<=17 :
    print('status anda remaja')
elif usia<=30 : 
    print('status anda masih muda')
elif usia<=60 :
    print('status anda sudah dewasa')
else :
    print('status anda sudah lansia')