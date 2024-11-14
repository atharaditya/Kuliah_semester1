program membalik_nama;
uses crt;
type larik = array [1..100] of char;
var sk1 : larik;
    a : char;
    index1,jml_huruf1,i : integer;
begin
     clrscr;
     index1 := 1;
     write('Nama anda : ');
     while (a<> ' ') do
           begin
           a := readkey;write(a);
           sk1[index1] := a ;
           index1 := index1+1;
           end;
               jml_huruf1 := index1;
           writeln;
           write('Kebalikan : ');
for I := jml_huruf1 downto 1 do
    begin
         write(sk1[i]);
    end;
readln;
end.