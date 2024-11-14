program enumerasi;
uses crt;
type
    nama_bulan = (januari, februari, maret, april, mei, juni, juli,
                  agustus, september, oktober, november, desember);
var
   month : nama_bulan;
begin
     clrscr;
     writeln('nilai ordinal januari-desember');
     for month := januari to desember do
         writeln(ord(month));
         writeln;
         repeat until keypressed;
end.