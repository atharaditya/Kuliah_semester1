PROGRAM beli_disket;
USES CRT;
CONST dolar = 14524.50;
VAR jml_disket         : integer;
    harga_disket, total : real;
BEGIN
     CLRSCR;
     jml_disket:=3;
     harga_disket:=3500;
     total:= jml_disket * harga_disket;
     WRITELN('Harga Disket = Rp. ',total:0:2);
     WRITELN('Harga Disket = $ ',total/dolar:0:2);
     READLN;
END.