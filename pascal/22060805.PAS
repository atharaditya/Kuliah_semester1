program nilai_praktikum_pascal;
uses crt;
type larik_nilai = array [1..100] of integer;
     larik_nama = array [1..100] of string[30];
var nilai : larik_nilai;
    nama : larik_nama;
    i, k, total : integer;
begin
     clrscr;
     nilai[1]:=80;
     nilai[2]:=75;
     nilai[3]:=80;
     nilai[4]:=60;
     nilai[5]:=85;
     nilai[6]:=80;
     nilai[7]:=90;
     nilai[8]:=85;
     nilai[9]:=90;
     nilai[10]:=100;
     nama[1]:='Andi     ';
     nama[2]:='Bambang  ';
     nama[3]:='Basuki   ';
     nama[4]:='Cahyono  ';
     nama[5]:='Dadang   ';
     nama[6]:='Endah    ';
     nama[7]:='Gara     ';
     nama[8]:='Naruto   ';
     nama[9]:='Sakura   ';
     nama[10]:='Sasuke  ';

     writeln('Daftar nilai praktikum pascal');
     for i := 1 to 10 do
     begin
          total := total + nilai[i];
     end;
     for k := 1 to i do
     writeln(nama[k], nilai[k]);
     writeln('Nilai rata-rata adalah ',total/10:0:2);
     readln;
end.
