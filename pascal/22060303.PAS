program nilai_rata_rata;
uses crt;
var a,b,c,total,jumlah:integer;
    rata:real;
begin
     clrscr;
     writeln;
     gotoxy(11,2);
     writeln('          rata-rata nilai dari 3 mahasiswa');
     gotoxy(9,3);
writeln('==================================================');
writeln;
write('nama');
gotoxy(25,5);
writeln('nilai');
writeln;
write('Atha:');gotoxy(26,7);readln(a);
writeln;
write('Gilang:');gotoxy(26,9);readln(b);
writeln;
write('Adil:');gotoxy(26,11);readln(c);
writeln;
     total:=3;
     jumlah:=a+b+c;
     rata:=jumlah/total;
     write('rata-rata: ');
     gotoxy(1,25);write(rata:0:2);
     readkey
end.
