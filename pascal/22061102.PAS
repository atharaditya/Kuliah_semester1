program tebakan;
uses crt;
var bilangan, tebak : integer;
begin
     clrscr;
     randomize;
     bilangan := random(10) + 1;
     writeln('Saya memiliki sebuah bilangan antara 1-10. coba tebak! ');
     repeat
           write('Tebakan anda adalah : '); readln(tebak);
           if tebak <> bilangan then
              writeln('Tebakan salah. Coba tebak lagi.')
           else
               writeln('Kamu is the best. Tebakanmu tepat.');
     until(tebak = bilangan);
     readln;
end.