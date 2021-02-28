{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_tres;

var
a,i:integer;

begin
writeln('Este programa mostra a tubuada(multiplicacao) de 1 a 10 do numero inteiro informado.');
writeln('Digite um numero inteiro para ser mostrada a tabuada dele.');readln(a);
//como nao ha restricao alguma no comando, o numero pode ser negativo ou nulo tambem.
writeln();
writeln('TABUADA DO ',a,' (multiplicacao)');

for i:= 1 to 10 do
begin
writeln(a,' x ',i,' = ',a*i);
end;

readln();
end.
