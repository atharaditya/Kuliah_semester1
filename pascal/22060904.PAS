program mengalikan_matriks;
uses crt;
var
   a,b,c : array [1..50, 1..50] of integer;
   i,j,k,x,y,z : integer;
   begin
        clrscr;
        writeln('Mengalikan dua matriks');
        writeln;

        writeln('Input data matriks A');
        write('Baris : ');readln(x);
        write('Kolom : ');readln(y);
        writeln;

        writeln('Input data matriks B');
        write('Baris : ');
        writeln(y);
        write('Kolom : ');readln(z);
        writeln;

        for i:=1 to x do
        for j:=1 to y do
            begin
                 write('Matriks A[',i,',',j,']:');readln(a[i,j]);
            end;
        writeln;

        for i:=1 to y do
        for j:=1 to z do
            begin
                 write('Matriks B[',i,',',j,']:');readln(b[i,j]);
        end;
        for i:=1 to x do
        for j:=1 to z do
        for k:=1 to y do

        c[i,j]:=c[i,j]+a[i,k]*b[k,j];
        writeln;

        for i:=1 to x do
        begin
             for j:=1 to z do
             write(c[i,j],'');
             writeln;
        end;
   readln;
end.