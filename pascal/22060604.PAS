program urut;
uses crt;
var i : integer;
begin
     clrscr;
     for i := 1 to 10 do
     begin
          gotoxy(40,i);
          write(i:10);
     end;
     readln;
end.