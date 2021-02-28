{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program dez_seis;
var
a,aux:real; //valor digitado e temporario
i: integer;

begin
aux:=-2;
i:=1;
writeln('Este programa identifica o maior valor digitado de uma serie de numeros.');
writeln('Informe 0 ',i,chr(167),' valor da serie.');readln(a);
while a<0 do
begin
writeln('Somente serao reconhecidos valores positivos (inclusive no ',i,chr(167),' termo).');readln(a);
end;

while a<>-1 do
begin
if a>aux then aux:= a;
i:=i+1;
writeln('Digite o ',i,chr(167),' valor (-1 para encerrar).');readln(a);
while (a<0)and(a<>-1) do
begin
writeln('Nao sao aceitos valores negativos (exceto -1)');
writeln('Digite o ',i,chr(167),' valor (-1 para encerrar).');readln(a);
end;
end;

writeln();
writeln('Maior valor digitado = ',aux:0:2);

readln();
end.
