string = ""
bar = 1

x = int(input("Masukkan angka untuk membentuk segitiga:"))

while bar <= x:
	kol = bar	
	while kol > 1:
		string = string + "   "
		kol = kol - 1

	kanan = 0
	while kanan <= (x - bar):
		string = string + " * "
		kanan = kanan + 1	
		
	string = string + "\n"
	bar = bar + 1
print (string)