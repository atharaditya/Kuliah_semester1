//Program menghitung kuas lingkaran

#include<iostream>
#include<iomanip>
#include<windows.h>

main()
{
	float luas,phi = 3.14;
	int r;
	
	std::cout<<"Program menghitung luas lingkaran"<<std::endl;
	std::cout<<"------------------------"<<std::endl;
	std::cout<<std::endl;
	std::cout<<"Diketahui: "<<std::endl;
	std::cout<<"Jari-jari =";std::cin>>r;
	
		luas = phi*r*r;
		
	system("CLS");
	std::cout<<"Jadi hasil perhitungan luas lingkaran"<<std::endl;
	std::cout<<"Adalah:"<<std::endl;
	std::cout<<"Luas lingkaran ="<<std::fixed\
			 <<std::setprecision(2)<<luas;
}
