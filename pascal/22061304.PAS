program data_record;
uses crt;
type
    mahasiswa = record
       nim : string[15];
       ipk : real;
    end;
    larik = array [1..15] of mahasiswa;
var
   mhs : larik; i, jml_mhs : integer;
begin
     clrscr;
     writeln('Program pendaftaran asisten praktikum pemrograman 1');
     write('Berapa data yang ingin dimasukan? (1-15)?' );
     readln(jml_mhs);
     for i := 1 to jml_mhs do
     begin
       write('NIM : ');readln(mhs[i].nim);
       write('IPK : ');readln(mhs[i].ipk);
       if mhs[i].ipk <= 2.75 then
       writeln('Maaf,anda(',mhs[i].nim,')tidak diterima.');
       writeln;
end;
writeln;
write('Data ke berapa yang ingin ditampilkan? (1-15)? ');
readln(i);
if i > jml_mhs then
   writeln('Data ke- ',i,' tidak bisa ditampilkan')
else if mhs[i].ipk <= 2.75 then
     writeln('Maaf data ke- ',i,' tidak memenuhi syarat')
     else
         begin
              writeln('NIM : ',mhs[i].nim);
              writeln('IPK : ',mhs[i].ipk:0:2);
         end;
     readln;
end.