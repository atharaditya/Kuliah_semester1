program bilangan_ganjil;
uses crt;
var i, total : integer;
begin
     clrscr;
     i := 1;
     write('deret bilangan ganjil : ');
     repeat
           write(i, ' ');
           i := i + 2;
           total := total + i;

     until(i>100);
     writeln;
     writeln('jumlah total : ',total);
     readln;
end.