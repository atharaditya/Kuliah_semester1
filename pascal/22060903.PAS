program matriks2x4;
uses crt;
type
    matriks = array [1..2, 1..4] of integer;
var
   A,B : matriks; i,j,k : integer;
begin
     clrscr;
     A[1,1]:=6;   A[1,2]:=1;   A[1,3]:=4;   A[1,4]:=8;
     A[2,1]:=4;   A[2,2]:=5;   A[2,3]:=2;   A[2,4]:=1;

     B[1,1]:=9;   B[1,2]:=3;   B[1,3]:=8;   B[1,4]:=5;
     B[2,1]:=7;   B[2,2]:=1;   B[2,3]:=4;   B[2,4]:=2;
     write('Matriks A');writeln;
             for i := 1 to 2 do
     begin
             for j := 1 to 4 do write(A[i,j]:4);writeln;
     end;
     writeln;

     writeln('Matriks B');write;
begin
     clrscr;
     A[1,1]:=6;   A[1,2]:=1;   A[1,3]:=4;   A[1,4]:=8;
     A[2,1]:=4;   A[2,2]:=5;   A[2,3]:=2;   A[2,4]:=1;

     B[1,1]:=9;   B[1,2]:=3;   B[1,3]:=8;   B[1,4]:=5;
     B[2,1]:=7;   B[2,2]:=1;   B[2,3]:=4;   B[2,4]:=2;
     writeln('Matriks A');writeln;
             for i := 1 to 2 do
     begin
             for j := 1 to 4 do write(A[i,j]:4);writeln;
     end;
     writeln;

     writeln('Matriks B');write;
             for i := 1 to 2 do
     begin
             for k := 1 to 4 do write(A[i,k]+B[i,k]:4);writeln;
     end;
readln;
end;
end.

