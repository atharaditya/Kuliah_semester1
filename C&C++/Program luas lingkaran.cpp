//program luas_lingkaran

#include<stdio.h>
#include<stdlib.h>

main()
{
	float luas,phi = 3.14;
	int r;
	
	printf("Program menghitung luas lingkaran\n");
	printf("Diketahui;\n");
	printf("jari-jari =");scanf("%d",&r);
	
		luas = phi*r*r;
	
	printf("Jari-jari = %d\n",r);
	printf("Maka;\n");
	printf("luas lingkaran = %.2f\n",luas);
	
	system("pause");
	system("cls");
}
