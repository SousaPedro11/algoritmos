{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_dez;
var
a,b,soma: array [1..9999] of real;
i,j,n: integer;

begin
writeln('Este programa recebe e soma dois vetores de tamanho N.');
writeln('Informe o tamanho dos vetores (numero de elementos).');readln(n);
writeln();
while n<=0 do
begin
writeln('Valor invalido. Informe o tamanho dos vetores (tamanho > 0)');readln(n);
writeln();
end;
//SetLength(a,n+1);
//SetLength(b,n+1);
//SetLength(soma,n+1);

for i:= 1 to 2 do
begin
	for j:= 1 to n do
	begin
		if i=1 then
		begin
		writeln('Escreva o elemento a',j,' do vetor A');readln(a[j]);
		end
		else
		begin
		writeln('Escreva o elemento b',j,' do vetor B');readln(b[j]);
		soma[j]:=a[j]+b[j];
		end;
	end;
	writeln();
end;

for i:=1 to 3 do
begin
writeln();
case i of
1: write('VETOR A = [ ');
2: write('VETOR B = [ ');
else
write('VETOR SOMA = [ ');
end;
	for j:=1 to n do
	begin
		case i of
		1: write(a[j]:0:2,' ');
		2: write(b[j]:0:2,' ');
		else
		write(soma[j]:0:2,' ');
		end;
	end;
writeln(']');
end;
readln();
end.
