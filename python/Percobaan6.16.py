#Contoh penggunaan Nested loop
#menampilkan bilangan prima
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, "adalah bilangan prima")
    i = i + 1

print("Yeah programnya Berhasil")