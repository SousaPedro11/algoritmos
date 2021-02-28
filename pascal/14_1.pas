{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_um;
var
veta,vetb: array[1..5] of integer;
i,j: integer;

begin
writeln('Este programa inverte a ordem dos elementos do vetor informado.');
j:=0;
for i:= 1 to 5 do
begin
writeln('Digite o elemento a',i,' do vetor');readln(veta[i]);
end;

for i:= 5 downto 1 do
begin
j:=j+1;
vetb[j]:=veta[i];
end;

for i:= 1 to 2 do
begin
writeln();
case i of
1: write('VETOR INFORMADO --> [ ');
else
write('VETOR INVERTIDO --> [ ');
end;

	for j:= 1 to 5 do
	begin
		case i of
		1: write(veta[j],' ');
		else
		write(vetb[j],' ');
		end;
	end;
writeln(']');
end;

readln();
end.
