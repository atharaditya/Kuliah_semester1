program memilih_nama_hari;
uses crt;
var hari : integer;
begin
     clrscr;
     writeln('program memilih nama-nama hari');
     write('masukan angka: ');readln(hari);
     case hari of
          1 : writeln('hari senin');
          2 : writeln('hari selasa');
          3 : writeln('hari rabu');
          4 : writeln('hari kamis');
          5 : writeln('hari jumat');
          6 : writeln('hari sabtu');
          7 : writeln('hari minggu');
          end;
          readln;
end.