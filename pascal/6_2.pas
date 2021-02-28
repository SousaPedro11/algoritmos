{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_dois;

var
base, altura: real;//declara variaveis

begin
writeln('Este programa calcula a area de um retangulo, para isso necessita-se da base e altura.');//imprime mensagem
writeln('Digite o valor da base do retangulo'); readln (base);//le base
//condicao para entrada
while base<=0 do
begin
writeln('Entrada invalida! A base deve ser maior que 0');
writeln('Insira novamente o valor da base');readln(base);
end;

writeln('Digite o valor da altura do retangulo'); readln (altura);//le altura
//condicao de entrada
while altura<=0 do
begin
writeln('Entrada invalida! A altura deve ser maior que 0');
writeln('Insira novamente o valor da altura');readln(altura);
end;

writeln();
writeln('A area do retangulo de base = ',base:0:2,' e altura = ', altura:0:2,' e igual a ',base*altura:0:2, ' UA (unidades de area).');//imprime saida
readln();
end.
