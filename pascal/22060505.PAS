program memilih_nama_bulan;
uses crt;
var bulan : integer;
begin
     clrscr;
     writeln('program memilih nama-nama bulan');
     write('masukan angka: ');readln(bulan);
     case bulan of
          1 : writeln('bulan januari');
          2 : writeln('bulan februari');
          3 : writeln('bulan maret');
          4 : writeln('bulan april');
          5 : writeln('bulan mei');
          6 : writeln('bulan juni');
          7 : writeln('bulan juli');
          8 : writeln('bulan agustus');
          9 : writeln('bulan september');
          10 : writeln('bulan oktober');
          11 : writeln('bulan november');
          12 : writeln('bulan desember');
     end;
     readln;
end.