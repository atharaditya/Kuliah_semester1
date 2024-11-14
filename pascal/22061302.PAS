program myrecord;
uses crt;
type
    ktm = record
        nama          : string[15];
        nim           : string[20];
        tempat_lahir  : string[30];
        tgl_lahir     : string[20];
        jenis_kelamin : string[20];
        jurusan       : string[30];
        prodi         : string[30];
        semester      : char;
    end;
var
   Atha : ktm;
begin
   clrscr;
   Atha.nama := 'Atha Nala Isra Raditya';Atha.tgl_lahir := '13 September 2004';
   Atha.nim  := '3202216006';            Atha.jenis_kelamin := 'laki-laki';
   Atha.tempat_lahir := 'Surakarta';     Atha.jurusan := 'Teknik Elektro';
   Atha.prodi := 'Teknik Informatika';   Atha.semester := '1';
   gotoxy(30,1);
   writeln('Kartu Tanda Mahasiswa');
   writeln;
   writeln('Nama           : ',Atha.nama);
   writeln('Nim            : ',Atha.nim);
   writeln('Tempat lahir   : ',Atha.tempat_lahir);
   writeln('Tanggal lahir  : ',Atha.tgl_lahir);
   writeln('Jenis kelamin  : ',Atha.jenis_kelamin);
   writeln('Jurusan        : ',Atha.jurusan);
   writeln('Prodi          : ',Atha.prodi);
   writeln('Semester       : ',Atha.semester);
   readln;
end.
