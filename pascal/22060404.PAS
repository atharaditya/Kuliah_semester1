program ganjil_genap;
uses crt;
var bil : integer;
begin
     clrscr;
     writeln('masukan bilangan ganjil dan genap');
     write(' masukan angka (0-65535) : ');
     readln(bil);
if bil mod 2= 0 then
     writeln('bilangan genap')
else
     writeln('bilangan ganjil');
     readln;
end.