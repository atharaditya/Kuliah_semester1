program deret_angka_ganjil;
uses crt;
var
   i, a : integer;
begin
     clrscr;
     i := 1;
     write('masukan bilangan tertinggi : ');readln(a);

     write('deret bilangn ganjil : ');
     repeat
           write(i, ' ');
           i := i + 2;
     until(i>a);
     writeln;
     readln;
end.