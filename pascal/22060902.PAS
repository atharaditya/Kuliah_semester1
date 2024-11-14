program matriks3x2;
uses crt;
type
    matriks = array [1..3, 1..2] of integer;
var
   A,B : matriks; i,j,k : integer;
begin
     clrscr;
     A[1,1]:=1;   A[1,2]:=4;   B[1,1]:=-5;  B[1,2]:=2;
     A[2,1]:=3;   A[2,2]:=9;   B[2,1]:=5;   B[2,2]:=3;
     A[3,1]:=6;   A[3,2]:=7;   B[3,1]:=2;   B[3,2]:=6;

     writeln('Matriks A');
     writeln;
                for i := 1 to 3 do
     begin
                for j := 1 to 2 do write(A[i,j]:5);writeln;
     end;
     writeln;
     writeln('Matriks B');
                for i := 1 to 3 do
     begin
                for k := 1 to 2 do write(B[i,k]:5);writeln;
     end;
     writeln;

     writeln('Hasil');writeln;
                for i := 1 to 3 do
     begin
                for k := 1 to 2 do write(A[i,k]+B[i,k]:5);writeln;
     end;
readln;
end.




