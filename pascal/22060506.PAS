program nilai;
uses crt;
var n : char;
    k : string;
begin
     clrscr;
     write('masukan nilai anda (A-E) : ');readln(n);
     case n of
     'A' : k:='istimewa';
     'B' : k:='baik';
     'C' : k:='cukup';
     'D' : k:='kurang';
     'E' : k:='tidak lulus';
     'F'..'Z' : k:='nilai yang anda masukkan salah!';
     end;
     writeln(k);
     readln;
end.