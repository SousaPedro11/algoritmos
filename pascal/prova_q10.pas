{
UNIVERSIDADE FEDERAL DO PARA
INSTITUTO DE CIENCIAS EXATAS E NATURAIS
FACULDADE DE COMPUTACAO - CURSO DE BACHARELADO EM SISTEMAS DE INFORMACAO
DISCIPLINA: ALGORITMOS
PROFA: MARCELLE MOTA
ESTUDANTE: PEDRO PAULO LISBOA DE SOUSA / 201711140038
}

program prova_q10;
var
a:array [1..10] of integer; //declara a com vetor de 10 posicoes inteiras
i,aux:integer; //contador e auxiliar de troca
troca:boolean; //se v, ordenado; se f, falta ordenar

begin
writeln('Este programa ordena em ordem decrescente um vetor de 10 posicoes.');
writeln();

//le os elementos do vetor de 10 posicoes
for i:= 1 to 10 do
begin
writeln('Informe o elemento a',i,' do vetor');readln(a[i]);
end;
writeln();

//imprime vetor inserido
write('VETOR INSERIDO = [');
for i:= 1 to 10 do
write(a[i],' ');
writeln(']');

//ordena vetor decrescente
repeat
troca:=true;
            for i:=1 to 9 do
            if a[i]<a[i+1] then
            begin
            aux:=a[i];
            a[i]:=a[i+1];
            a[i+1]:=aux;
            troca:=false;
            end
until troca;

writeln();

//escreve vetor ordenado
write('VETOR DECRESCENTE = [');
for i:= 1 to 10 do
write(a[i],' ');
writeln(']');

readln();
end.
