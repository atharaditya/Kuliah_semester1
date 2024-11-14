PROGRAM nilai_maksimal;
USES CRT;
VAR a, b, max : integer;
BEGIN
     CLRSCR;
     TEXTCOLOR(lightblue);
     WRITE('masukan bilangan pertama : ');READLN(a);
     WRITE('masukan bilangan kedua   : ');READLN(b);
     IF a>b THEN
        max:=a
     ELSE
         max:=b;
     WRITELN('bilangan terbesar adalah ',max);
     READLN;
END.