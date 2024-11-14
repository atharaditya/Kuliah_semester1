import os
os.system("cls")
import time
import datetime
import os

print('-'*50)
print('Selamat datang di ATM BANK TOYIB. silahkan buat akun terlebih dahulu.')
print('-'*50)
nama = input("masukkan nama anda : ")
rek=(input("masukkan nomor rekening anda : "))
no_pin=int(input("masukkan pin : "))
tabungan = (int(input("silahkan nominal yang ingin anda tabung : ")))
os.system('cls')
print('='*50)
print('Akun Telah dibuat silahkan masukkan kembali pin anda')
pin = int(input("Masukkan Nomor Pin : "))
print('Tunggu sebentar ya...')
time.sleep(0.5)
if pin == no_pin:
    while True :
        os.system("cls")
        print('='*50)
        print("Selamat Datang di ATM BANK TOYIB. Silahkan buat akun terlebih dahulu")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Yok Nabung")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            os.system("cls")
            print("")
            print('='*50)
            print(datetime.datetime.now())
            print("Nama anda : ",nama)
            print("No rekening : ",rek)
            print('tunggu sebentar...')
            time.sleep(0.5)
            print('='*50)
            print('\t\tSTRUK BANK TOYIB')
            print('='*50)
            print(datetime.datetime.now())
            print('\t\t\tNama : ',nama)
            print('\t\t\tOpsi : Cek Saldo')
            print("Sisa Saldo anda adalah Rp.",tabungan,'\n')
            print('\t\tTerima Kasih')
            print('='*50)
            print("")
            lagi = input("Apakah Kamu Ingin Mencoba Lagi? (y/n) : ")
            if lagi == "n" or lagi == "N":
                break
        elif a == 2:
            os.system("cls")
            print('='*50)
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            tf=int(input("Masukkan Rekening Tujuan : "))
            Transfer = (int)(input("Masukan Nominal Yang Mau DiTransferkan : "))
            if Transfer <= tabungan:
                tabungan = tabungan - Transfer
                print("")
                print(datetime.datetime.now())
                print("Nama anda : ",nama)
                print("No rekening : ",rek)
                print("Tujuan Rekening : ",tf)
                print('tunggu sebentar...')
                time.sleep(0.5)
                print('='*50)
                print('\t\tSTRUK BANK TOYIB')
                print('='*50)
                print(datetime.datetime.now())
                print('\t\t\tNama : ',nama)
                print('\t\t\tOpsi : Transfer Uang')
                print("\t\t\tTujuan Rekening : ",tf)
                print("Sisa Saldo anda adalah Rp.",tabungan,'\n')
                print('\t\tTerima Kasih')
                print("")
                print('='*50)
                lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
                if lagi == "n" or lagi == "N":
                    break
            else:
                print("Maaf Niat Anda Baik, Tapi Saldo anda tidak mencukupi")
                lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
                if lagi == "n" or lagi == "N":
                    break
        elif a == 3:
            os.system("cls")
            nominal = (int(input("Nominal Yang Akan Di Tarik : ")))
            if nominal <= tabungan:
                tb=tabungan-nominal
                print('='*50)
                print('Nama anda : ',nama)
                print('No rekening : ',rek)
                print(datetime.datetime.now())
                time.sleep(0.5)
                print('='*50)
                print('\t\tSTRUK BANK TOYIB')
                print('='*50)
                print(datetime.datetime.now())
                print('\t\t\t\tNama : ',nama)
                print('\t\t\t\tOpsi : Tarik Uang')
                print('\t\t\t\tNominal ditarik : ',nominal)
                print("Sisa Saldo anda adalah Rp.",tb,'\n')
                print('\t\tTerima Kasih')
                print('='*50)
                print("")
                lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
                if lagi == "n" or lagi == "N":
                    break
            else:
                print("Maaf Nominal Yang Anda Tarik Kurang Dari Tabungan Anda")
                lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
                if lagi == "n" or lagi == "N":
                    break
            
        elif a == 4:
            os.system("cls")
            print('='*50)
            nabung = int(input("Masukkan Nominal Yang Akan Dimasukkan : "))
            tb2 = tabungan + nabung
            print("")
            print(datetime.datetime.now())
            print("Nama anda : ",nama)
            print("No rekening : ",rek)
            print('tunggu sebentar...')
            time.sleep(0.5)
            print('='*50)
            print('\t\tSTRUK BANK TOYIB')
            print('='*50)
            print(datetime.datetime.now())
            print('\t\t\tNama : ',nama)
            print('\t\t\tOpsi : Tabung Uang')
            print('\t\t\tAnda Menabung sebesar : ',nabung)
            print("Sisa Saldo anda adalah Rp.",tb2,'\n')
            print('\t\tTerima Kasih')
            print('='*50)
            print("")
            lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
            if lagi == "n" or lagi == "N":
                break
        elif a == 5:
            print("Terima Kasih Sudah Memakai Program Kami")
            break
        else:
            print("pilihan tidak tersedia")
            lagi = input("Apakah Kamu Ingin Mencoba Lagi (y/n) : ")
            if lagi == "n" or lagi == "N":
                break       
else:
    print("Maaf Pin Yang Anda Masukkan Salah, Silahkan menginput ulang dari awal")
    exit()