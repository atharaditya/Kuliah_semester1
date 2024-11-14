program pembayaran_pajak;
uses crt;
var gaji,pkp,nilai : longint;
    pembayaran : real;
    nama       : string;
begin
     clrscr;
     nilai :=360000;
     writeln(' PROGRAM PEMBAYARAN PAJAK ');
     writeln('==========================');
     write('nama        : ');readln(nama);
     write('gaji        : Rp. ');readln(gaji);
    if gaji>nilai then
     begin
     pkp:=gaji-nilai;
     pembayaran:=pkp/10;
     writeln('anda wajib membayar pajak sebesar : ',pembayaran :0:2);
     end
    else
    writeln('anda tidak wajib membayar pajak');
    readln;
end.