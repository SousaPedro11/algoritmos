program treze_um;
var
vet: array[1..10] of integer;
i,j,aux: integer;

begin
writeln('Este programa le um vetor de 10 posicoes e coloca em ordem crescente');
writeln();
writeln('Insira os valores para as 10 posicoes do vetor');
for i:= 1 to 10 do
begin
read(vet[i]);
end;

writeln();
write('VETOR INSERIDO: [ ');
for i:= 1 to 10 do
begin
write(vet[i],' ');
end;
writeln(']');

for i:= 10 downto 2 do
begin
	for j:= 1 to i-1 do
	begin
		if vet[j] > vet[j+1] then
		begin
		aux:=vet[j];
		vet[j]:=vet[j+1];
		vet[j+1]:=aux
		end;
	end;
end;

writeln();
write('VETOR ORDENADO: [ ');
for i:= 1 to 10 do
begin
write(vet[i],' ');
end;
writeln(']');

readln();
end.
