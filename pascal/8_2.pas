{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_dois;
var
a:integer;

begin
writeln('Este programa mostra se o numero digitado e par ou impar');
writeln('Digite um numero inteiro');readln(a);

if (a mod 2) = 0 then
writeln('Este numero e par')
else
writeln('Este numero e impar');
readln();
end.
