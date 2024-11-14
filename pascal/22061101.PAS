program repeat_until;
uses crt;
var i : integer;
begin
  clrscr;
  i := 3;
  repeat
    writeln(i:10);
    inc(i);
  until(i > 10);
  readln;
end.