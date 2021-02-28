{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_cinco;

var
distancia,consumo:real;//declara variaveis

begin
//entrada distancia
writeln('Este programa calcula o consumo de gasolina em em km/l.');
writeln('Digite o valor da distancia percorrida em km.'); readln(distancia);
//condicao entrada
while distancia<=0 do
 begin
 writeln('A distancia deve ser maior que 0.');
 writeln();
 writeln('Digite o valor da distancia percorrida.'); readln(distancia);
 end;
//entrada consumo
writeln('Digite o total de combustivel gasto'); readln(consumo);
//condicao entrada
while consumo<=0 do
 begin
 writeln('O tanto de combustivel gasto ser maior que 0.');
 writeln();
 writeln('Digite o valor do combustivel consumido.'); readln(consumo);
 end;
//saida
 writeln();
 writeln('O consumo medio em km/l ---> ', distancia/consumo:0:2); readln();
end.
