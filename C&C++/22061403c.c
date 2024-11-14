//Menghitung luas lingkaran

#include<stdio.h>
#include<stdlib.h>

#define PHI 3.14

main()
{
	float luas;
	int r;
	
	printf("Program menghitung luas lingkaran\n");
	printf("---------------------------------\n");
	printf("\n");
	printf("Diketahui : \n");
	printf("Jari-jari = ");scanf("%d",&r);
		
		luas = PHI*r*r;
		
	system("cls");
	printf("Jadi hasil perhitungan luas lingkaran\n");
	printf("Jika jari-jari = %d\n",r);
	printf("Maka : \n");
	printf("Luas lingkaran = %.2f\n",luas);
}
