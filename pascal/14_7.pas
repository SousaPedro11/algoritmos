{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_sete;
var
a: array [1..9999] of real;
i,n,pos: integer;
maior: real;

begin
writeln('Este programa recebe N numeros, armazena num vetor e mostra qual o maior digitado.');
writeln();
writeln('Informe quantos numeros serao digitados.');readln(n);
while n<=0 do
begin
writeln('Valor invalido. Qunatos numeros serao digitados? (quantidade > 0)');readln(n);
writeln();
end;
//SetLength(a,n+1);

maior:=-9999;
for i:= 1 to n do
begin
writeln('Informe o valor do elemento a',i);readln(a[i]);
	if a[i]>maior then
	begin
	pos:=i;
	maior:=a[i];
	end;
end;

writeln();
writeln('Maior elemento --> a',pos,' = ', maior:0:2);
readln();
end.
