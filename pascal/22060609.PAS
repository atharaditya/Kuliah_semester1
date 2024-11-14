program menghitung_pangkat;
uses crt;
var a, b, c : integer;
begin
     clrscr;
      writeln('program menghitung pangkat');
      writeln('--------------------------');
      write  ('masukan nilai yang akan dihitung: ');readln(a);
      write  ('masukan nilai pangkat: ');readln(b);
      writeln;
      c:=1;
     for b:= 1 to b do
      c:=c*a;
     writeln ('jadi, hasilnya adalah ',c);
     readln;
end.