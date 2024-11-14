program deret_fibonacci;
uses crt;
type larik = array [1..100] of integer;
var deret: larik;
    n, a : integer;
begin
     clrscr;
     write('Masukan jumlah deret : ');readln(n);
     writeln;
     for a := 0 to n-1 do
     begin
          if (a = 0) or (a = 1) then
             begin
                  deret[a]:=1;
                  write(deret[a],' ');
             end
          else
              begin
                   deret[a]:=deret[a-1]+deret[a-2];
                   write(deret[a],' ');
              end;
          end;
     readln;
end.