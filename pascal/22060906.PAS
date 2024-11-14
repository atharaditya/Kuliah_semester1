program data_mahasiswa;
uses crt;
type
    larik1 = array [1..15] of string;
    larik2 = array [1..10,1..3] of real;
var
   nama    : larik1;
   nilai   : larik2;
   total,k : real;
   jml_mhs,i,j : integer;
   ket : string;
begin
     clrscr;
     writeln('DATA MAHASISWA');
     writeln;
     write('berapa jumlah mahasiswa (max 15 orang)?');
     readln(jml_mhs);
     for i:= 1 to jml_mhs do
     begin
          clrscr;
          write('nama mahasiswa : '); readln(nama[i]);
          for j := 1 to 3 do
          begin
               write('masukan nilai ke-',j,'');
               readln(nilai[i,j]);
          end;
     end;
     clrscr;
     writeln('DATA MAHASISWA');
     writeln;
     for i := 1 to jml_mhs do
     begin
          writeln(i,'.',nama[i]);
     for j := 1 to 3 do;
     write('nilai :',nilai[i,j] :0:2);
     writeln;
     ket := 'lulus';
     if (nilai[i,j] < 60.00) then ket:= 'tidak lulus';
     writeln('keterangan : ',ket);
     end;
     readln;
end.
