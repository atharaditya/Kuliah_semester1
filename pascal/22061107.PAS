program deret_bilangan_fibonacci;
uses crt;
var a,b,c,d,total : integer;
begin
     clrscr;
     write('masukan bilangan tertinggi : ');readln(d);
     write('deret bilangan fiboncci : ');
     a := 1;
     b := 1;
     repeat
           total := total + a;
           write(a,' ');
           c := a +b;
           a := b;
           b := c;
     until(a>d);
     writeln;
     writeln('total dari bilangan fibonacci adalah : ',total);
     readln;
end.