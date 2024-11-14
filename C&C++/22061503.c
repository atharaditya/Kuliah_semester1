//program ganjil genap

#include <stdio.h>

main()
{
	int bil;
	
	printf("Program menentukan bilangan genap atau ganjil\n");
	printf("Masukan sebuah bilangan! ");scanf("%d",&bil);
	printf("\n");
	
	if(bil%2==0)
		printf("Bilangan %d yang anda masukan adalah genap!",bil);
	else
		printf("Bilangan %d yang anda masukan adalah ganjil!",bil);
}
