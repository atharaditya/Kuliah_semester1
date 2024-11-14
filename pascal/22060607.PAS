program akumulator;
uses crt;
var accumulator, i, n : integer;
begin
     clrscr;
     accumulator:=0;
     n:=10;
     for i := 1 to n do
         accumulator:=accumulator+i;
     writeln('nilai pengumpul atau akumulator adalah : ', accumulator);
     readln;
end.