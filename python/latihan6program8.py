string = ""
bar = 1

x = int(input("Masukan angka untuk membentuk segitiga: "))
print("\n")

while bar <= x:
    kol = bar

    while kol > 1:
        string = string + "   "
        kol = kol - 1

    kiri = 0 
    while kiri <= (x - bar):
        string = string + " * "
        kiri = kiri + 1

    kanan = kiri
    while kanan > 1:
        string = string + " * "
        kanan = kanan - 1

    string = string + "\n\n"
    bar = bar + 1
print(string)