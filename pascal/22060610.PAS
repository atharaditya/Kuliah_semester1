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
    writeln('旼컴컴컴컴컴컫컴컴컴컴컴컴컴컴컴컴컴쩡컴컴컴컴컴컴컴컴컴컴컴�');
    writeln('�   bulan    �   saldo awal bulan   �   saldo akhir bulan   �');
    writeln('쳐컴컴컴컴컴컵컴컴컴컴컴컴컴컴컴컴컴탠컴컴컴컴컴컴컴컴컴컴컴�');
    gotoxy(1,5);
    writeln('�   Januari  �   '); gotoxy(30,5);writeln('       �'); gotoxy(50,5);writeln('           �');
    writeln('�   Februari �   '); gotoxy(30,6);writeln('       �'); gotoxy(50,6);writeln('           �');
    writeln('�   Maret    �   '); gotoxy(30,7);writeln('       �'); gotoxy(50,7);writeln('           �');
    writeln('읕컴컴컴컴컴컨컴컴컴컴컴컴컴컴컴컴컴좔컴컴컴컴컴컴컴컴컴컴컴�');

    readln;
end.