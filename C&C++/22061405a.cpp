//Input Output Pemrograman C++

#include <iostream>
#include <iomanip>

int main()
{
	float a;
	
	std::cout << "Masukkan sebuah nilai: ";std::cin >> a;
	std::cout << "Nilai yang dimasukkan adalah : " \
                      << std::setprecision(8) << a ;
}
