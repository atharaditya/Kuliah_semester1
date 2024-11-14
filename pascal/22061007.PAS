program jumlah;
uses crt;
var a,b : string; c,d : char; e,f : integer;
begin
     clrscr;
     write('Masukan kalimat! ');
     e := 1;
     while (c<>#13) do
begin
     c := readkey;
     if (c=#8) then
        begin
             if (length(b)=0) then continue;
             delete (b, length(b),1);
                    write(c);
                    continue;
             end;
             e:= 1;
             while (c <> #13) do
begin
     c:= readkey;
     if (c=#8) then
     begin
     if (length(b)=0) then
     continue;
     delete(b,length(b),1);
     write(c);
     continue;
     end;
     b:= b+c;
     write(c);
     if c= ' ' then e := e+1;
     end;
writeln('Ketikan sebuah kalimat : ',b);
writeln('Jumlah kata yang anda masukan adalah : ',e,' kata');
readln;
end;
end.