i = 1
batas = 5

if i < batas:
    iDua = i + 1
    if iDua < batas:
        iTiga = iDua + 1
        if iTiga < batas:
            iEmpat = iTiga + 1
            if iEmpat < batas:
                iLima = iEmpat + 1
                # dan seterusnya
                print(iLima)
            print(iEmpat)
        print(iTiga)
    print(iDua)
print(i)

print()
print()

def AngkaTampil(batas, i=1):
    prefix = '--' * (i - 1)

    print(f'{prefix} Sebelum rekursif({i})')
    if (i < batas):
    #disinilah rekursifitas itu terjadi
        AngkaTampil(batas, i+1)

    print(f'{prefix} Setelah rekursif ({i})')
#memanggil fungsi AngkaTampil
#untuk pertama kali
AngkaTampil(5)