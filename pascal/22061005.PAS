program password;
uses crt;
var c : char;
    i,kesalahan,j : integer;
    pass : string;
const
     proteksi = '123';
     proteksi1= ' 123';
begin
     clrscr;
     c := 'a';
     kesalahan := 1;
     while (kesalahan<=3) do
     begin
          write('Masukan password : ');
          while (c<> #13) do
          begin
          c := readkey;
          if c <> #13 then
          write('*'); pass := pass + c;
          end;
     writeln;
     if pass = proteksi + c then
     begin
          kesalahan := 4;
          writeln('BENAR');
          end
     else
     begin
          writeln('Password salah. Ulangi sekali lagi!');
          inc(kesalahan);
          c := 'a';
          for j:= 1 to length(pass) do
             delete(pass,length(pass),1);
     end;
     writeln;
     end;
     readln;
end.