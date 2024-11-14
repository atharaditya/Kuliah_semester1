program myrecord;
uses crt;
type
    pohon = record
      daun : integer;
      batang : real;
      akar : string[20];
    end;
var
   mangga : pohon;
begin
     clrscr;
     mangga.daun := 500;
     mangga.batang := 60.3;
     mangga.akar := 'tunggang';
     writeln('ini adalah data-data pohon mangga saya');
     writeln('jumlah daun ',mangga.daun:8);
     writeln('diameter batang : ',mangga.batang:8:2);
     writeln('jenis akar : ',mangga.akar);
     readln;
end.