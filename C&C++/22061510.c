    // Program Menghitung Luas dan Keliling Bidang Datar

    #include <stdio.h>
    #include <stdlib.h>

    main()
    {
       int datar,i;
       char menu,ulang,satuan[3];
       float sisi,Luas1;

       ulang:
       printf("Selamat Datang Di \n");
     printf("Program Menghitung Luas dan Keliling Bidang \
     Datar\n");
     printf("\n");
     printf("Menu: \n");
     printf("1. Persegi.\n");
     printf("2. Persegi Panjang.\n");
     printf("3. Lingkaran.\n");
     printf("4. Segitiga.\n");
     printf("5. Keluar.\n");
     printf("\n");
     printf("Pilih Angka 1 .. 4 Untuk Mulai Menghitung Luas \
     dan Keliling Bidang Datar! ");
     scanf("%d",&datar);
     system("cls");

     switch (datar)
     {
	case 1:
	  printf("Program Menghitung Luas dan Keliling \
       Persegi.\n");
	  printf("\n");
	  printf("Pilih: \n");
	  printf("A. Menghitung Luas Persegi.\n");
	  printf("B. Menghitung Keliling Persegi.\n ");
	  scanf("%c",&menu);
	  printf("Pilihan Anda adalah: ",menu);
	  system("cls");

	  switch (menu)
	  {
	    case 'A':
	    printf("A. Menghitung Luas Persegi\n");
	    printf("Masukkan Nilai Satuan yang akan dipakai! ");
	    scanf("%s",&satuan);
	    printf("Masukkan Nilai Sisi Persegi! ");
	    scanf("%f",&sisi);
	    Luas1 = sisi * sisi;
	    printf("Luas Persegi adalah %.2f ",Luas1);
	    printf("%s persegi.\n",satuan);
	    break;
	    case 'B':
	    printf("B. Menghitung Keliling Persegi\n");
	    break;
	  }
	  break;
	  case 2:
	    printf("Menghitung Luas dan Keliling Persegi \
         Panjang.\n");
	    break;
	  case 3:
	    printf("Menghitung Luas dan Keliling Lingkaran.\n");
	    break;
	  case 4:
	    printf("Menghitung Luas dan Keliling Segitiga.\n");
	    break;
	  default:
	    printf("Angka yang Anda masukkan salah!!!");
       }
     }

