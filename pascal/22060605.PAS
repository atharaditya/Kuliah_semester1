program urut_angka;
uses crt;
var i : integer;
begin
     clrscr;
     for i := 100 to 400 do
     begin
          if i mod 100=0 then
             writeln(i);
     end;
     readln;
end.