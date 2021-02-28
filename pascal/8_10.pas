{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_dez;

var
cod,quant:integer;
nome:string;
preco:real;

begin
writeln('Este programa mostra o  cardapio e calcula o valor do lanche.');
writeln();
writeln('	   CARDAPIO');
writeln('CODIGO  ITEM		   PRECO');
writeln(' 100    Cachorro Quente    R$1.10');
writeln(' 101    Bauru Simples      R$1.30');
writeln(' 102    Bauru com Ovo      R$1.50');
writeln(' 103    Hamburguer         R$1.10');
writeln(' 104    Cheeseburguer      R$1.30');
writeln(' 105    Refrigerante       R$1.00');

writeln();
writeln('Insira o codigo do pedido');readln(cod);
while (cod<100)or(cod>105) do
begin
writeln('Insira um codigo de pedido valido (de 100 a 105)');
readln(cod);
end;

writeln('Informe a quantidade do pedido.');readln(quant);
while quant<0 do
begin
writeln('A quantidade deve ser maior que zero. Insira outro valor');
readln(quant);
end;

case cod of
100: begin
nome:='Cachorro Quente';
preco:=1.10;
end;
101: begin
nome:='Bauru Simples';
preco:=1.30;
end;
102: begin
nome:='Bauru com Ovo';
preco:=1.50;
end;
103: begin
nome:='Hamburguer';
preco:=1.10;
end;
104: begin
nome:='Cheeseburguer';
preco:=1.30;
end;
else
 begin
nome:='Refrigerante';
preco:=1.00;
end;
end;

writeln();
writeln('ITEM: ',nome);
writeln('QTDE: ',quant);
writeln('PRECO: R$',quant*preco:0:2);
readln();
end.
