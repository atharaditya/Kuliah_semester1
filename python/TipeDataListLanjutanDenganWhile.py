barang = []
stop = False
i = 0

print(">>>>> Selamat Datang di AITI MART <<<<<")
print("Silahkan masukan barang belanjaan Anda!")

while(not stop):
    barang_baru = str(input("Masukan barang yang ke-{}: ".format(i)))
    barang.append(barang_baru)

    i += 1

    tanya = str(input("Mau mengisi keranjang belanja lagi? (y/t):"))
    if(tanya == "t"):
        stop = True

print("~"*30)
print("Kamu belanja sebanyak {} barang".format(len(barang)))
for barangku in barang:
    print("-{}".format(barangku))
print("~"*30)