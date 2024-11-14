program while_do;
uses crt;
var
   i:integer;
begin
   clrscr;
   i:=1;
   writeln('menmpilkan angka 1 sampai 10');
   while i <= 10 do
         begin
              write(i,' ');
              i:= i + 1;
         end;
         readln;
end.