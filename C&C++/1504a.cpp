//program if...else

#include <stdio.h>
#include <stdlib.h>

main()
{
	float a,b,c,D,x1,x2;
	
	//masukan nili a,b,c untuk menghiung determinan
	printf("Masukan nilai a! ");scanf("&f",&a);
	printf("Masukan nilai b! ");scanf("&f",&b);
	printf("Masukan nilai c! ");scanf("&f",&c);
	
	//perhitungan determinan
	D = b*b - 4*a*c;
	
	//seleksi nili determinan
	if(D==0){
		x1 = -b/ (2*a);
		printf("D=0 akan menghasilkan dua akar real kembar\n");
		printf("x1 = x2 = %f\n",x1);	
	}
	else if(D>0){
		x1 = (-b + (sqrt(D))) / (2*a);
		x2 = (-b - (sqrt(D))) / (2*a);
		printf("D>0 akan menghsilkan dua akar real berlainan\n");
		printf("x1 = %f\n",x1);
		printf("x2 = %f\n",x2);
	}
	else if(D<0){
		x1 = -b / (2*a);
		x2 = sqrt(-D)/ (2*a);
		printf("D<0 akan menghasilkan dua akar real berlainan\n");
		printf("x1 = %.2f + %.2f i\n",x1,x2);
		printf("x2 = %.2f - %.2f i\n",x1,x2);
	}

}
