program treze_dois;
var
mat: array[1..3,1..3] of integer;
i,j,par,impar: integer;

begin
par:=0;
impar:=0;
writeln('Este programa le uma matriz 3x3 e mostra o numero de elementos pares e impares');
writeln();
for i:= 1 to 3 do
begin
writeln('Insira os 3 valores da ',i,' linha.');
	for j :=1 to 3 do
	begin
	read(mat[i,j]);
		if (mat[i,j] MOD 2) = 0 then
		par:=par+1
		else
		impar:=impar+1;
	end;
	end;
writeln();

{//Mostra matriz
for i:= 1 to 3 do
begin
write('| ');
for j :=1 to 3 do
begin
write(mat[i,j],' ');
end;
writeln('|');
end;
}

writeln('Nº de Pares = ',par,' (',(100*par/(par+impar)):0:2,'%)');
writeln('Nº de Impares = ',impar,' (',(100*impar/(par+impar)):0:2,'%)');
readln();
end.
