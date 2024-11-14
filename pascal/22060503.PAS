program nilai_ujian;
uses crt;
var nilai : integer;
begin
     clrscr;
     write('tulis nilai ujian anda (0-100) : ');readln(nilai);
     sound(500); delay(1000); nosound;
     case nilai of
     80..100 : writeln('anda mendapat nilai A');
     70..79 : writeln('anda mendapat nilai B');
     60..69 : writeln('anda mendapat nilai C');
     20..59 : writeln('anda mendapat nilai D');
     0..19 : WRITELN('anda mendapat nilai E');
     else writeln('mohon maaf, nilai yang anda masukan salah !')
     end;
     readln;
end.