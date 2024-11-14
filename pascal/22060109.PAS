 program luas_lingkaran;
 uses crt;
 const phi = 3.14;
 var r : integer;
     luas : real;
 begin
      clrscr;
      writeln('program menghitung luas lingkaran');
      writeln('diketahui :');
      write('     jari-jari = ');readln(r);
      luas:=phi*r*r;
      writeln('     phi = ',phi);
      writeln('maka :');
      writeln('     luas lingkaran = ',luas);
      write('       luas lingkaran = ',luas:0:0);
      readln;
 end.