program deret_bilangan;
uses crt;
var karakter : char;
    baris, c, d, e, kolom : integer;
begin
     clrscr;
     write('masukan jumlah baris:');readln(c);
     for c := 1 to c do
     begin
          for d := 1 to c do
          begin
               write(d:2);
          end;
          e:=e+d;
          writeln(' = ',e:2);
     end;
     readln;
end.