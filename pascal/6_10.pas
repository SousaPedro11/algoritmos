{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_dez;

var//declara
salario, percent:real;

begin
writeln('Este programa calcula o valor do salario apos reajuste de x%.');
writeln();
//entrada
writeln('Informe o valor do salario atual.');readln(salario);
//condicao entrada
while salario<=0 do
begin
writeln('Informe um valor válido para o salario atual (>0).');
readln(salario);
end;
//entrada
writeln();
writeln('Informe o percentual de rajuste (sem o % ou decimal, ex: 4).'); readln(percent);
//saida
writeln();
writeln('Salario atual ---> ',salario:0:2);
writeln('Salario apos rajuste de ',percent:0:2,'% --->', salario*(1+percent/100):0:2);
readln();
end.
