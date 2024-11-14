string = ""
bar = 1

x = int(input("Masukan angka untuk memebentuk segitiga: "))
print("\n")

while bar < x:
    kol = bar
    while kol > 1:
        string = string + "   "
        kol = kol - 1
    kiri = 0
    while kiri <=(x - bar):
        string = string + " * "
        kiri = kiri + 1
    kanan = kiri 
    while kanan > 1:
        string = string + " * "
        kanan = kanan - 1

    if(bar+1) <= x:
        string = string + "\n\n"
    bar = bar + 1

bar = x-1

while bar >= 0:
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1 
    kiri = 1
    while kiri < (x - (bar-1)):
        string = string + " * "
        kiri = kiri + 1
    kanan = 1
    while kanan < kiri - 1:
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n\n"
    bar = bar - 1
print(string)