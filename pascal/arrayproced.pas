program arrayproced;
uses                //nao precisa disso
Crt;                //nem disso

type
arr= array [1..9999,1..9999] of real;   //defini arr como uma matriz 9999x9999


var
m,n:integer;      //numero de linhas e colunas da matriz
mat: arr;         //defini map como tipo arr (uma matriz 9999x9999)

procedure leit(a,b:integer; var mat:arr);   //inicio da procedure (a e b receberao os valores de m e n)
var
i,j:integer;   //contadores de loop i linhas e j colunas
begin
//gotoxy(6,5);  <- nao precisa disso
writeln('Leitura dos elementos');
     for i:=1 to a do
     begin
          for j:=1 to b do
          begin
          write('Escreva o elemento a[',i,j,'] da matriz.');readln(mat[i,j]);
          end;
     end;
writeln();
end;

procedure escr(a,b:integer; var mat:arr);   //procedure de escrita
var
i,j:integer;
begin
//gotoxy(6,a*b+6);
writeln('Matiz A (',a,'x',b,')');
     for i:=1 to a do
     begin
//     gotoxy(3,a*b+6+i);
     write('| ');
          for j:=1 to b do
          begin
          write(mat[i,j]:0:2,' ');
          end;
     writeln('|')
     end;
end;

//programa principal
begin
writeln('Este programa le e imprime uma matriz MxN.');
write('Informe o numero de linhas da matriz (M linhas)');readln(m); //pede m linhas
while m<1 do
begin
write('Informe um numero valido para a quantidade de linhas!(M>=1)');readln(m);
end;
write('Informe o numero de colunas da matriz (N linhas)');readln(n);//pede n colunas
while n<1 do
begin
write('Informe um numero valido para a quantidade de linhas!(M>=1)');readln(n);
end;

writeln();
leit(m,n,mat);   //chama a procedure de leitura mxn retornando mat
escr(m,n,mat);   //chama a procedure de escrita mxn escrevendo mat

readln();
end.
