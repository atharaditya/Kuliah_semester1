program deret_bilangan;
uses crt;
var karakter : char;
    baris, i, j, kolom : integer;
begin
     clrscr;
     for i := 1 to 5 do
     begin
          for j := 1 to i do
          begin
               textcolor(i);
               write(j:2);
          end;
          writeln;
     end;
     readln;
end.