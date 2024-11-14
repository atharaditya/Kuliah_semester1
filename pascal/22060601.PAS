program ulang_nama;
uses crt;
var i : integer; nama : string[30];
begin
     clrscr;
     nama:='Soekarno-Hatta';
     for i :=1 to 5 do
         writeln(nama);
     readln;
end.