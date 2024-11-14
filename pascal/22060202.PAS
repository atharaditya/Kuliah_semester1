program identitas;
uses crt;
var nama : string[10];
    ipk : real;
    semester : byte;
    sex : boolean;
begin
     clrscr;
     nama:='Atha Nala Isra Raditya';
     sex:=true;
     semester:=1;
     ipk:=3.80;
     writeln('nama saya : ', nama);
     writeln('true = laki-laki');
     writeln('false = perempuan');
     writeln('jenis kelamin : ', sex);
     writeln('semester : ', semester,' (ganjil)');
     writeln('ipk saya = ', ipk:2:2);
     readln;
end.