{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_tres;
var
a:integer;

begin
writeln('Este programa calcula o gasto com macas da seguinte forma:');
writeln('Se a quantidade comprada for menor que 12, o preco unitario e R$1.30');
writeln('Se forem compradas pelo menos 12, o valor unitario e R$1.00.');
writeln();
writeln('Digite a quantidade de macas compradas');readln(a);
if a<12 then
writeln('O custo total da compra sera --> R$', a*1.30:0:2)
else
writeln('O custo total da compra sera --> R$', a*1.00:0:2);
readln();
end.
