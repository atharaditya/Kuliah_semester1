program enumerasi;
uses crt;
type
    nama_saudara = (atha, agra);
var
    nama : nama_saudara;
begin
    clrscr;
    writeln('nilai ordinal nama saudara');
    for nama := atha to agra do
         writeln(ord(nama));
    writeln;
    writeln('atha memiliki 2 saudara');
    writeln('atha anak ke- ',ord(atha));
    writeln('setelah atha adalah anak ke- ',ord(succ(atha)));
    repeat until keypressed;
end.