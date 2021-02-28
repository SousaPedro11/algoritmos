{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_dois;
var
a:integer;

begin
writeln('Este programa imprime uma ordem decrescente ate 1, a partir de um valor informado.');
writeln('Informe um valor inteiro');readln(a);

while a<=1 do
begin
writeln('O valor deve ser maior que 1. Insira outro valor.');readln(a);
end;

writeln('Ordem Decrescente (de ',a,' ate 1)');

repeat
write(a,' ');
a:=a-1
until a<1;

readln();
end.
