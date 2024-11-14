program palindrom;
uses crt;
var kata,kata_awal,kata_akhir : string;
    i,j : integer;
begin
     clrscr;
     writeln('===============================================');
     writeln('============PROGRAM KATA PALINDROM=============');
     writeln('===============================================');
     writeln;
     write('silahkan masukan kata : ');readln(kata);
     writeln;
     j:= length(kata);
     kata_awal := ' ' ;
     for i := 1 to j do
         kata_awal:=kata_awal+kata[i];
     for i := j downto 1 do
         kata_akhir:=kata_akhir+kata[i];
     writeln('Kata awalnya : ',kata_awal,' Dibalik menjadi : ',kata_akhir);
     writeln;
     if kata_awal = kata_akhir
     then
     writeln('Kata tersebut bukan merupakan kata Palindrom')
     else
     writeln('Kata tersebut merupakan kata Palindrom');
     readln;
end.