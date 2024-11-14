# program 6 pengecekan potongan harga

print('Program diskon')
print('==============')
print()
print('Struk belanjaan toko Garuda Mart')
print('Jl. Komyos Sudarso, komp TNI-AL, no.74')
tanggal_transaksi = bool(input('Tanggal transaksi: '))
waktu_transaksi = bool(input('Waktu transaksi : jam '))
print('Nama kasir : Atha Nala Isra Raditya ')
nama_pelanggan = str(input('Nama pelanggan: '))
total_belanja = int(input('Total belanja : Rp. '))
if (total_belanja >= 50000) and (total_belanja < 150000) :
    harga_akhir = total_belanja - (0.1*total_belanja)
    print(f'Anda mendapat diskon sebesar 5%, Total belanja anda Rp. {total_belanja} Anda cukup membayar sebesar Rp. {harga_akhir} Terima kasih telah berbelanja di toko kami')
elif (total_belanja >= 150000) and (total_belanja < 250000) :
    harga_akhir = total_belanja - (0.2*total_belanja)
    print(f'Anda mendapat diskon sebesar 10%, Total belanja anda Rp. {total_belanja} Anda cukup membayar sebesar Rp. {harga_akhir} Terima kasih telah berbelanja di toko kami')
else :
    harga_akhir = total_belanja - (0.3*total_belanja)
    print(f'Anda mendapat diskon sebesar 15%, Total belanja anda Rp. {total_belanja} Anda cukup membayar sebesar Rp. {harga_akhir} Terima kasih telah berbelanja di toko kami')