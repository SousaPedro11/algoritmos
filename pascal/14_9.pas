{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_nove;
var
a,b: array [1..10] of real;
i: integer;
x: real;

begin
writeln('Este programa recebe um vetor de 10 posicoes e multiplica por uma variavel X; ambos inseridos pelo usuario.');
writeln();

writeln('Insira o valor da variavel que multiplicara o vetor.');readln(x);
writeln();
for i:= 1 to 10 do
begin
writeln('Insira o valor do elemento a',i,' do vetor.');readln(a[i]);
b[i]:=a[i]*x;
end;

writeln();
write('Vetor A = [ ');
for i:= 1 to 10 do
begin
write(a[i]:0:2,' ');
end;
writeln(']');

writeln();
write('Vetor A*',x:0:2,' = [ ');
for i:= 1 to 10 do
begin
write(b[i]:0:2,' ');
end;
writeln(']');
readln();
end.
