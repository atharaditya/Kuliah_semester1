program urut_angka;
uses crt;
var i : integer ; angka : string[30];
begin
     clrscr;
     for i :=1000 to 4000 do
     begin
          if i mod 1000=0 then
             write(i:85);
     end;
     readln;
end.