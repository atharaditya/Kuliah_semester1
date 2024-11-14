//Menghitung luas lingkaran

#include<stdio.h>
#include<stdlib.h>

main()
{
	float luas, phi = 3.14;
	int r;
	
	printf("Program menghitung luas lingkaran\n");
	printf("---------------------------------\n");
	printf("\n");
	printf("Diketahui : \n");
	printf("Jari-jari = ");scanf("%d",&r);
		
		luas = phi*r*r;
		
	system("clc");
	printf("Jadi hasil perhitungan luas lingkaran\n");
	printf("Jika jri-jri = %d\n",r);
	printf("Maka : \n");
	printf("Luas lingkaran = %.2f\n",luas);
}
