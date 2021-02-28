{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_oito;

var//declara variaveis
dolar,cotacao:real;

begin
writeln('Este programa converte dolar em real.');
writeln('Para tal e necessario informar o valor em dolar e a cotacao.');
writeln('ex: cotacao no dia 19/05/17 ---> 3.2872.');
writeln();
//entrada dolar
writeln('Informe a quantidade de dolares a ser convertida.'); readln(dolar);
//condicao entrada
while dolar<=0 do
begin
writeln('Digite um valor valido para a quantidade de dolares(>0).');
writeln('Informe a quantidade de dolares a ser convertida.'); readln(dolar);
end;
//entrada cotacao
writeln('Informe a cotacao do dolar no dia.'); readln(cotacao);
//condicao entrada
while cotacao<=0 do
begin
writeln('Digite um valor valido para a cotacao(>0).');
writeln('Informe a cotacao do dolar no dia.'); readln(cotacao);
end;
//saida
writeln();
writeln(dolar:0:2,' Dolares ---> ', dolar*cotacao:0:2,' Reais.');
readln();
end.
