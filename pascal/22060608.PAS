program tampil_ascii;
uses crt;
var huruf : char; i : integer;
begin
     clrscr;
     for i := 1 to 10 do
     begin
          write('tulis sebuah huruf : ');
          huruf:=readkey;
          writeln('kok hurufnya tidak muncul?');
          sound(300); delay(1000); nosound;
          sound(600); delay(1500); nosound;
          writeln;
          writeln('huruf yang anda masukan adalah huruf ',huruf);
          writeln('no ascii dr huruf di atas adalah ',ord(huruf));
     end;
     readln;
end.