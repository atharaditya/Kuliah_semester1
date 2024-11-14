baris = int(input("masukan jumlah baris: "))
a = (baris * (baris + 1))//2

b = [1,1]
for i in range(2,a):
    num = b[-1] + b[-2]
    b.append(num)
num = 0

for i in range(0,baris):
    for j in range(0,i +1):
        print(b[num], "",end="")
        num = num + 1
    print()