program deret_angka_genap;
uses crt;
var
   i, a : integer;
begin
     clrscr;
     write('masukan bilangan tertinggi : ');readln(a);

     write('deret bilangn genap : ');
     repeat
           write(i, ' ');
           i := i + 2;
     until(i>a);
     writeln;
     readln;
end.