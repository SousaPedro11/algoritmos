{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_cinco;
var
a,i,fat:integer; //valor, contador e fatorial

begin
writeln('Este programa calcula o fatorial de um numero inteiro.');
writeln('Digite o valor cujo fatorial sera fatorado.');readln(a);

while a<0 do
begin
writeln('O numero nao pode ser negativo! Informe novamente.');readln(a);
end;

if a=0 then
fat:=1
else
begin
fat:= a;//inicializacao de fat
for i:=1 to (a-1) do
begin
fat:= fat*(a-i)
end;
end;

writeln();
writeln('Fatorial de ',a,' (',a,'!) = ',fat);
readln();
end.
