string = ""
bar = 1

x = int(input("Masukan angka untuk membentuk segitiga: "))

while bar <= x:
    kol = bar

    while kol > 0:
        string = string + " * "
        kol = kol - 1

    string = string + "\n"
    bar = bar + 1
print(string)