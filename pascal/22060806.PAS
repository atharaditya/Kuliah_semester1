program bilangan;
uses crt;
type larik_bil = array [1..10] of integer;
var jml          : larik_bil;
    besar,kecil,k,n,jumlah,b,c  : integer;
    rata         : real;
begin
     clrscr;
     n:=10;
     jumlah:=0;
     for k :=1 to n do
     begin
          write('Masukan bilangan ke-',k,': ');readln(jml[k]);
          jumlah:=jumlah+jml[k];
     end;
     besar:=jml[1];
     kecil:=jml[1];
      for k := 1 to n do
      begin
           if jml[k] > besar then
           begin
           besar:=jml[k];
           b:=k
           end
           else
           if jml[k] > kecil then
           begin
           kecil:=jml[k];
           c:=k
           end;
      end;
     rata:=jumlah/n;
     writeln;
     writeln('Bilangan terbesar : ',besar,' dan terletak pada urutan ke-',b);
     writeln('Bilangan terkecil : ',kecil,' dan terletak pada urutan ke-',c);
     writeln('Rata-rata bilangan : ',rata:0:0);
     readln;
end.