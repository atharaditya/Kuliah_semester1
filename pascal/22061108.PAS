program bilangan_genap;
uses crt;
var i, total : integer;
begin
     clrscr;
     i := 2;
     write('deret bilangan genap :');
     repeat
           write(i, ' ');
           total := total + i;
           i := i + 2;
     until(i>100);
     writeln;
     writeln('jumlah total : ',total);
     readln;
end.