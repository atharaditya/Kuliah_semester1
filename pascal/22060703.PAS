program deret_bilangan;
uses crt;
var karakter : char;
    baris, i, j, kolom : integer;
begin
     clrscr;
     for i := 1 to 3 do
     begin
          for j := 1 to 10 do
          begin
               textcolor(i);
               write('1');
          end;
          writeln;
     end;
     readln;
end.