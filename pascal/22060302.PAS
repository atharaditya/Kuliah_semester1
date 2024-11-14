PROGRAM mencari_luas_lingkaran;
USES CRT;

CONST
phi =3.14;
VAR
luas,jejari:real;
BEGIN
CLRSCR;
WRITELN('MENCARI_LUAS_LINGKARAN');
WRITELN('======================');
WRITE('masukan jari-jari lingkaran : ');
READLN(jejari);
luas:=phi*sqr(jejari);
WRITELN('luas lingkaran adalah          :',round(luas));
READLN;
END.