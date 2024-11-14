program tebakan;
uses crt;
var bilangan, tebak, jumlah_tebakan : integer;
begin
     clrscr;
     randomize;
     bilangan := random(10) + 1;
     writeln('Saya memiliki sebuah bilangan antara 1-10. coba tebak! ');
     repeat
           write('Tebakan anda adalah : '); readln(tebak);
           if tebak <> bilangan then
           begin
              writeln('Tebakan salah. Coba tebak lagi.');
              inc(jumlah_tebakan)
           end
           else
           begin
               writeln('Kamu is the best. Tebakanmu tepat.');
               writeln('jumlah tebakan kamu adalah : ',jumlah_tebakan,' kali');
           end;
     until(tebak = bilangan);
     readln;
end.