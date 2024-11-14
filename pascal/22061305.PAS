program data_record;
uses crt;
type
    mahasiswa = record
      nama : string[30];
      nim  : string[10];
      ipk  : real;
    end;
    larik = array[1..15] of mahasiswa;
var
   mhs : larik; i, jml_mhs,krng,lbh : integer;
   min,max,rata,tot : real;
   nim : string;
begin
     clrscr;
     writeln('program memasukan data mahasiswa');
     write('berapa data yang akan dimasukkan (1-15)? ');
     readln(jml_mhs);
     min := 4;
     max := 0;
     for i := 1 to jml_mhs do
     begin
          write('nama: '); readln(mhs[i].nama);
          write('nim : '); readln(mhs[i].nim);
          write('ipk : '); readln(mhs[i].ipk);
     if (max < mhs[i].ipk) then
        begin
        max := mhs[i].ipk;
        nim := mhs[i].nim;
     end;
     if (min > mhs[i].ipk) then
        min := mhs[i].ipk;

     if (mhs[i].ipk < 2.50) then
        inc(krng);

     if (mhs[i].ipk >= 2.50) then
        inc(lbh);

     tot := tot+mhs[i].ipk;
     rata := tot/jml_mhs;
   end;
     writeln;
     writeln('IPK tertinggi = ',max:0:2);
     writeln('IPK terendah = ',min:0:2);
     writeln('NIM Mahasiswa dengan ipk tertinggi = ',nim);
     writeln('Rata-rata IPK = ',rata:0:2);
     writeln('jumlah mahasiswa dengan IPK < 2.50 = ',krng);
     writeln('jumlah mahasiswa dengan IPK > 2.50 = ',lbh);
     readln;
end.