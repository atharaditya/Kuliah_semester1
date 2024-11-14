program gaji_karyawan;
uses crt;
var gol : byte;
    gt1, gt2, gt3, gt4, gt5, gt6, gt7, t1, t2, t3, t4, t5, t6, t7 : real;
const g1=100000; tj1=0.05;
      g2=120000; tj2=0.1;
      g3=150000; tj3=0.13;
      g4=175000; tj4=0.17;
      g5=200000;
      g6=220000;
      g7=250000;
begin
     clrscr;
     t1:=g1*tj1; t2:=g2*tj2;
     t3:=g3*tj2; t4:=g4*tj2;
     t5:=g5*tj2; t6:=g6*tj3;
     t7:=g7*tj4;
     gt1:=g1+t1; gt2:=g2+t2;
     gt3:=g3+t3; gt4:=g4+t4;
     gt5:=g5+t5; gt6:=g6+t6;
     gt7:=g7+t7;
     write('berapa golongan anda? ');readln(gol);
     case gol of
     1 : writeln('gaji pokok        :  ',g1:2);
     2 : writeln('gaji pokok        :  ',g2:2);
     3 : writeln('gaji pokok        :  ',g3:2);
     4 : writeln('gaji pokok        :  ',g4:2);
     5 : writeln('gaji pokok        :  ',g5:2);
     6 : writeln('gaji pokok        :  ',g6:2);
     7 : writeln('gaji pokok        :  ',g7:7);
     else
     end;
     case gol of
     1 : writeln('tunjangan jabatan :  ',t1:0:2);
     2 : writeln('tunjangan jabatan :  ',t2:0:2);
     3 : writeln('tunjangan jabatan :  ',t3:0:2);
     4 : writeln('tunjangan jabatan :  ',t4:0:2);
     5 : writeln('tunjangan jabatan :  ',t5:0:2);
     6 : writeln('tunjangan jabatan :  ',t6:0:2);
     7 : writeln('tunjangan jabatan :  ',t7:0:2);
     else
     end;
     case gol of
     1 : writeln('gaji total        : ',gt1:0:2);
     2 : writeln('gaji total        : ',gt2:0:2);
     3 : writeln('gaji total        : ',gt3:0:2);
     4 : writeln('gaji total        : ',gt4:0:2);
     5 : writeln('gaji total        : ',gt5:0:2);
     6 : writeln('gaji total        : ',gt6:0:2);
     7 : writeln('gaji total        : ',gt7:0:2);
     else
     end;
     readln;
end.
