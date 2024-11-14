//program IF tunggal sederhana dengan blok statement
#include <stdio.h>
#include <stdlib.h>

main() 
{
	float gaji_kotor,gaji_bersih,persen_tunjangan,tunjangan;
	int jlh_anak;
	
	printf("Berapa gaji anda? ");scanf("%f",&gaji_kotor);
	printf("Berapa jumlah anak anda? ");scanf("%d",&jlh_anak);
	
	if (jlh_anak >= 3)
	{
		persen_tunjangan = 0.3;
		printf("besar tunjangan yang anda peroleh adalah : %.0f",persen_tunjangan*100);
		printf("%%\n");
	}
		
	tunjangan = persen_tunjangan * gaji_kotor;
	gaji_bersih = gaji_kotor + tunjangan;
	
	printf("Gaji kotor anda sebesar = Rp. %.2f\n",gaji_kotor);
	printf("Tunjangan yang anda peroleh sebesar = Rp. %.2f\n",tunjangan);
	printf("Sehingga gaji yang anda peroleh adalah sebesar = Rp. %.2f\n",gaji_bersih);
	
}
