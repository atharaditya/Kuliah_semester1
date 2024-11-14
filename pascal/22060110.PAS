program menghitung_luas_segitiga;
uses crt;

var
alas,tinggi,luas:real;

begin
     clrscr;
     writeln('menghitung luas segitiga');
     writeln('========================');
     writeln('masukan nilai alas = ');
     readln(alas);
     writeln('masukan nilai tinggi = ');
     readln(tinggi);
     luas:=alas*tinggi/2;
     writeln('luas segitiga adalah =',luas:2:2);
     readln;
end.