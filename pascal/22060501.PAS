program nama_anak;
uses crt;
var no_anak : byte;
    na_anak : string;
begin
     clrscr;
     writeln('program untuk mengetahui nama anak keluarga hamid');
     write('tulis anak ke-');readln(no_anak);
     case no_anak of
          1 : writeln('anak ke-',no_anak,' bernama Azam');
          2 : writeln('anak ke-',no_anak,' bernama Sarah');
          3 : writeln('anak ke-',no_anak,' bernama Hasim');
          else writeln('hanya ada anak ke 1, 2, dan 3');
     end;
     writeln('nama anak ke-',no_anak,na_anak);
     readln;
end.