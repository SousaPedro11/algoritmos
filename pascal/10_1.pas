{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_um;

var
a,b:real;

begin
writeln('Este programa faz a divisao entre dois valores informados.');
writeln();
writeln('Informe o primeiro valor.');readln(a);
writeln('Informe o segundo valor.');readln(b);

while b=0 do
begin
writeln('O segundo valor nao pode ser 0. Digite outro valor.');readln(b);
end;


writeln(a:0:2,'/',b:0:2,' = ',a/b:0:2);

readln();
end.
