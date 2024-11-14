program isilarik;
uses CRT;
type
    larik = array [1..10] of string[30];
var nama : larik;
    i    : integer;
begin
     clrscr;
     nama[1]:='Ajis';
     nama[2]:='Nizar';
     nama[3]:='Gilang';
     nama[4]:='Afril';
     nama[5]:='Sinta';
     nama[6]:='Ririn';
     nama[7]:='Ilham';
     nama[8]:='Fellix';
     nama[9]:='Rifki';
     nama[10]:='Adil';
     for i := 1 to 10 do
       writeln ('Nama temanku ',nama[i]:2);
     readln;
end.