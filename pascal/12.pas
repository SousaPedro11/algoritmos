{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program doze;
var
a,b,c: array[1..3,1..3] of integer;// matriz a, b e matriz soma
i,j,k: integer; //linhas, colunas e matrizes(a, b ou c)

begin
writeln('Este programa soma duas matrizes 3x3.');

//loop para leitura e soma das matrizes
for k:= 1 to 2 do//varia matriz a e b
begin
     for i:= 1 to 3 do//linhas
     begin
          for j:=1 to 3 do//colunas
          begin
               if (k=1) then//condicao para sequencia matriz a ou b
              begin
               writeln('Escreva o valor para o elemento a',i,j,' da matriz A');
               readln(a[i,j]);
               end
               else
               begin
               writeln('Escreva o valor para o elemento b',i,j,' da matriz B');
               readln(b[i,j]);
               end;
c[i,j]:=a[i,j]+b[i,j]; //soma das matrizes
          end;
     end;
end;
writeln();

//loop para saida
for k:=1 to 3 do//selecao matriz a, b ou c
begin
//condicao do titulo da matriz escrita na tela
if k=1 then
writeln('MATRIZ A')
else if k=2 then
begin
writeln();
writeln('MATRIZ B')
end
else
begin
writeln();
writeln('MATRIZ SOMA (A+B)');
end;
//loop para escrever as matrizes
for i:=1 to 3 do//linhas
begin
write('| ');
     for j:=1 to 3 do//colunas
     begin
     if k=1 then
     write(a[i,j],' ')
     else if k=2 then
     write(b[i,j],' ')
     else
     write(c[i,j],' ');
     end;
writeln('|');
end;
end;
readln();
end.
