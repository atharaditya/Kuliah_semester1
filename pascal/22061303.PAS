program data_record;
uses crt;
type
    mahasiswa = record
      nama : string[30];
      nim  : string[7];
      ipk  : real;
    end;
    larik = array[1..15] of mahasiswa;
var
   mhs : larik; i, jml_mhs : integer;
begin
     clrscr;
     writeln('program memasukan data mahasiswa');
     write('berapa data yang akan dimasukkan (1-15)? ');
     readln(jml_mhs);
     for i := 1 to jml_mhs do
     begin
          write('nama: '); readln(mhs[i].nama);
          write('nim : '); readln(mhs[i].nim);
          write('ipk : '); readln(mhs[i].ipk);
     end;
     writeln;
     write('data ke berapa yang ingin ditampilkan (1-15)? ');
     readln(i);
     writeln('nama : ',mhs[i].nama);
     writeln('nim  : ',mhs[i].nim);
     writeln('ipk  : ',mhs[i].ipk);
     readln;
end.