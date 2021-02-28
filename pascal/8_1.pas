{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_um;
var
a:integer;

begin
writeln('Este programa mostra se o valor digitado e maior ou menor que 10');
writeln('Digite um numero inteiro');readln(a);
if a>10 then
writeln('E maior que 10')
else
begin
if a<10 then
writeln('E menor que 10')
else
writeln('E igual a 10')
end;
readln();
end.
