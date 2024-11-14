menu = 'Y' or 'y'
while menu == 'Y' or 'y' :
    print('Selamat Datang Di Resto Garuda Jaya')
    print('===================================')
    print()
    resto = str(input("Resto : "))
    alamat_resto = str(input("Alamat :"))
    pembeli = input("Masukkan nama Pembeli : ")
    nomor_meja = int(input("Nomor Meja : "))
    tanggal_transaksi = str(input('Tanggal transaksi : '))
    waktu_transaksi = str(input('Waktu transaksi : jam '))


    print('List Menu Makanan')
    print('=================')
    print('1. Nasi goreng biasa : Rp. 15.000')
    print('2. Nasi goreng telur : Rp. 16.000')
    print('3. Nasi goreng spesial : Rp. 18.000')
    print('4. Bakso : Rp. 13.000')
    print('5. Mie ayam : Rp. 12.000')
    listMenu = str(input('Masukan angka sesuai menu yang tersedia = '))
    jumlahPesanan= int(input('jumlah dibeli = '))
    if listMenu == '1':
        namaMakanan = 'Nasi goreng biasa'
        harga =(15000*jumlahPesanan)
        pajak = int(harga * 0.11)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == '2':
        namaMakanan = 'Nasi goreng telur'
        harga = (16000*jumlahPesanan)
        pajak = int(harga * 0.11)
        if jumlahPesanan >= 5:
            totalHarga = int(harga+pajak)
        else:
            totalHarga = int(harga+pajak)
    elif listMenu == '3':
        namaMakanan = 'Nasi goreng spesial'
        harga = int(18000*jumlahPesanan)
        pajak = int(harga * 0.11)
        totalHarga = int(harga+pajak)
    elif listMenu == '4':
        namaMakanan = 'Bakso'
        harga = int(13000&jumlahPesanan)
        pajak = int(harga * 0.11)
        totalHarga = int(harga+pajak)
    elif listMenu == '5':
        namaMakanan = 'Mie ayam'
        harga = int(12000*jumlahPesanan)
        pajak = int(harga * 0.11)
        totalHarga = int(harga+pajak)
    else:
        menu=input('Maaf, Menu yang dipilih tidak tersedia')
    
    print('List menu minuman')
    print('=================')
    print('1. es teh : Rp. 3.000')
    print('2. es jeruk : Rp. 5.000')
    print('3. kopi : Rp. 2.000')
    listMenu = str(input('Masukan angka sesuai menu yang tersedia = '))
    jumlahPesanan= int(input('jumlah dibeli = '))
    if listMenu == '1':
        namamimuman = 'es teh'
        harga =(3000*jumlahPesanan)
        pajak = int(harga * 0.11)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == '2':
        namaminuman = 'es jeruk'
        harga = (5000*jumlahPesanan)
        pajak = int(harga * 0.11)
        if jumlahPesanan >= 5:
            totalHarga = int(harga+pajak)
        else:
            totalHarga = int(harga+pajak)
    elif listMenu == '3':
        namamimuman = 'kopi'
        harga = int(2000*jumlahPesanan)
        pajak = int(harga * 0.11)
        totalHarga = int(harga+pajak)
    else:
        menu=input('Maaf, Menu yang dipilih tidak tersedia')

    print("=========================================")
    print("==============STRUK PESANAN==============")
    print("=============RESTO GARUDA JAYA===========")
    print("=========================================")
    print(" Nama Pelanggan          :", pembeli)
    print(" No Meja                 :", nomor_meja)
    print(" Menu Makanan            :", namaMakanan)
    print(" Jumlah Pesanan Makanan  :", jumlahPesanan)
    print(" Harga                   :", harga)
    print(" Pajak                   :", pajak)
    print(" Menu Minuman            :", namaminuman)
    print(" Harga                   :", harga)
    print(" Pajak                   :", pajak)
    print(" Total Pembayaran        :", totalHarga)
    print("==========================================")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")