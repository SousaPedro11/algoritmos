{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_quatro;

var
total, entrada:real;//declara variaveis

begin
writeln('Este programa calcula o valor da parcela de uma compra.');
writeln('O pagamento sera feito em 1+5 parcelas.');
writeln();
writeln('Digite o valor total da compra'); readln(total);//le valor total
//condicao entrada
while total<=0 do
 begin
 writeln('O valor total deve ser maior que 0.');
 writeln();
 writeln('Digite o valor total da compra'); readln(total);
 end;
 
writeln('Digite o valor da entrada'); readln(entrada);//le valor entrada
//condicao entrada
while (entrada>=total) or (entrada<=0) do
 begin
 if entrada<=0 then
 begin
 writeln('O valor da entrada deve ser maior que 0.');
 writeln();
 writeln('Digite o valor da entrada.'); readln(entrada);
 end
 else
 begin
 writeln('O valor da entrada deve ser menor que o total.');
 writeln();
 writeln('Digite o valor da entrada.'); readln(entrada);
 end;
 end;
//saida
writeln();
writeln('Total ---> ',total:0:2);
writeln('Entrada ---> ',entrada:0:2);
writeln('5 prestacoes de ---> ',(total-entrada)/5:0:2);
readln();
end.
