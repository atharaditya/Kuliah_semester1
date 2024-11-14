program tabel_tabungan;
uses crt;
var i : integer;
    jnr , jnrp : real;
begin
     clrscr;
     writeln('PROGRAM DATA TABUNGAN');
     jnr:=100000;
     {proses perulangan for to do}
     gotoxy(1,5);
     for i := 1 to 3 do
     begin
     jnrp := jnr*2/100+jnr;
     writeln(jnr:24:2, jnrp:20:2);
     jnr:=jnrp;
     end;
     {tabel penempatan}
     gotoxy(1,2);
    writeln('ÚÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿');
    writeln('³   bulan    ³   saldo awal bulan   ³   saldo akhir bulan   ³');
    writeln('ÃÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´');
    gotoxy(1,5);
    writeln('³   Januari  ³   '); gotoxy(30,5);writeln('       ³'); gotoxy(50,5);writeln('           ³');
    writeln('³   Februari ³   '); gotoxy(30,6);writeln('       ³'); gotoxy(50,6);writeln('           ³');
    writeln('³   Maret    ³   '); gotoxy(30,7);writeln('       ³'); gotoxy(50,7);writeln('           ³');
    writeln('ÀÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ');

    readln;
end.