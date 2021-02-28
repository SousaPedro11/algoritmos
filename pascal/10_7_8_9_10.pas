{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_7_8_9_10;
var
n,i,c:integer;//ntermos, contador e escolha(n vezes)
a:real;//somatorio

begin
writeln('Este programa calcula a serie: a= n + (n-1)/2 + (n-2)/3 + ... + 1/n; com n inteiro.');
writeln();
writeln('Escolha uma das opcoes abaixo digitando seu numero correspondente:');
writeln('1 - Somatorio com 10 termos (n=10).');
writeln('2 - Somatorio com 100 termos (n=100).');
writeln('3 - Somatorio com n termos (n definido pelo usuario).');
writeln();readln(c);
while (c<1)or(c>3) do
begin
writeln('Opcao invalida. Escolha as opcoes de 1 a 3.');readln(c);
end;

case c of
1: n:=10;
2: n:=100;
3: begin
	writeln('Informe de quantos termos sera o somatorio (n termos)');
	readln(n);
		while n<=0 do
		begin
		writeln('O numero de termos deve ser maior que zero. Informe o valor de n.');
		readln(n);
		end;
	end;
end;

a:=0;
for i:= 1 to n do
begin
a:=a+(n-i+1)/i;
end;

writeln();
writeln('Soma (A) = ',a:0:3);
readln();
end.
