program menghitung_luas_lingkaran;
uses crt;

const
phi =3.14;
var
luas,jejari:real;
begin
clrscr;
writeln('MENGHITUNG LUAS LINGKARAN');
writeln('==========================');
write('masukan jari-jari lingkaran : ');
readln(jejari);
luas:=phi*sqr(jejari);
writeln('luas lingkaran adalah      :',round(luas));
readln;
end.