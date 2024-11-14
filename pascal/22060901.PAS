program matriks3x4;
uses crt;
type
    matriks = array[1..3, 1..4] of integer;
var
   larik : matriks; i, j : integer;
begin
     clrscr;
     larik[1,1]:=10;      larik[1,2]:=2;
     larik[1,3]:=6;       larik[1,4]:=33;
     larik[2,1]:=17;      larik[2,2]:=5;
     larik[2,3]:=26;      larik[2,4]:=9;
     larik[3,1]:=11;      larik[3,2]:=-4;
     larik[3,3]:=31;      larik[3,4]:=18;
     for i :=1 to 3 do
     begin
          writeln ('Baris ke- ',i:5);
          for j := 1 to 4 do write(larik[i,j]*3:5); writeln;
     end;
     readln;
end.