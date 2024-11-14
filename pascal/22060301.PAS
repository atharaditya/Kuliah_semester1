program biodata;
uses crt;
var nama : string[20];
    umur : real;
    lama : integer;
    nilai : char;
begin
     clrscr;
     write('tulis nama anda : ');readln(nama);
     write('berapa umur anda : ');readln(umur);
     write('apa nilai ujian pascal anda (A-E)? ');
     nilai:=readkey;
     writeln('terima kasih... tunggu sebentar, ya...');
     lama:=1000;
     delay(lama);
     writeln;
     writeln('nama anda         : ',nama:20);
     writeln('umur anda         : ',umur:20:2);
     writeln('nilai anda        : ',nilai:20);
     gotoxy(20,24);
     write('tekan sembarang tombol');
     readln;
end.