{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_quatro;
var
a,b: array [1..10] of integer;
i,j: integer;

begin
writeln('Este programa recebe 10 numeros, armazena num vetor e imprime seus quadrados noutro vetor.');
writeln();

for i:=1 to 10 do
begin
writeln('Escreva o elemanto a',i,' do vetor');readln(a[i]);
b[i]:=sqr(a[i]);
end;

for i:=1 to 2 do
begin
writeln();
case i of
1: write('VETOR INSERIDO = [ ');
else
write('VETOR QUADRADO = [ ');
end;
	for j:=1 to 10 do
	begin
		case i of
		1: write(a[j],' ');
		else
		write(b[j],' ');
		end;
	end;
writeln(']');
end;

readln();
end.
