program isilarik;
uses CRT;
type
    larik = array [1..12] of string[30];
var bulan : larik;
    i     : integer;
begin
     clrscr;
     bulan[1]:='Januari';
     bulan[2]:='Februari';
     bulan[3]:='Maret';
     bulan[4]:='April';
     bulan[5]:='Mei';
     bulan[6]:='Juni';
     bulan[7]:='Juli';
     bulan[8]:='Agustus';
     bulan[9]:='September';
     bulan[10]:='Oktober';
     bulan[11]:='November';
     bulan[12]:='Desember';
         write('Tulis bulan ke- : ');readln(i);
         writeln('Bulan ke-',i,' adalah ',bulan[i]);
     readln;
end.