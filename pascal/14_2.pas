{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_dois;

var
a,b: array [1..9999] of integer;
i,j,n: integer;

begin
writeln('Este programa copia os elementos de um vetor a outro, o usuario informa o tamanho do vetor.');
writeln();
writeln('Informe o tamanho do vetor (maior que zero)');readln(n);
while n<=0 do
begin
writeln('Tamanho invalido! Digite um valor maior que zero.');readln(n);
end;
writeln();

//SetLength(a,n+1);   Funciona no compilador Geany(linux).
//SetLength(b,n+1);
for i:= 1 to n do
begin
writeln('Digite o elemento a',i);readln(a[i]);
b[i]:=a[i];
end;

for i:=1 to 2 do
begin
writeln();
case i of
1: write('VETOR a = [ ');
else
write('VETOR b = [ ');
end;
	for j:=1 to n do
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
