PROGRAM tanya;
USES CRT;
VAR a : real;
BEGIN
     CLRSCR;

     WRITE('masukan sebuah bilangan di bawah 100! ');
     READLN(a);
     IF a<100 THEN
              WRITE('terima kasih');
     READLN;
END.