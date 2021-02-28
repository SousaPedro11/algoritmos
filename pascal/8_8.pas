{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_oito;

var
n1,n2:string;
t1,t2:integer;

BEGIN
writeln('Este programa mostra o vencedor entre dois times.');
writeln('Para isso, deve-se informar o nome e gols de cada um.');
writeln();
writeln('Informe o nome do time 1');readln(n1);
writeln('Informe o numero de gols do time 1');readln(t1);

while t1<0 do
begin
writeln('O numero de gols nao pode ser negativo.');
writeln('Informe o numero de gols do time 1');readln(t1);
end;

writeln('Informe o nome do time 2');readln(n2);
writeln('Informe o numero de gols do time 2');readln(t2);

while t2<0 do
begin
writeln('O numero de gols nao pode ser negativo.');
writeln('Informe o numero de gols do time 2');readln(t2);
end;

writeln();

writeln('PLACAR: ',n1,' ', t1,' x ',t2,' ',n2);
writeln();
if t1>t2 then
begin
writeln('Time vencedor: ', n1);
writeln('Numero de gols: ', t1)
end
else
if t2>t1 then
begin
writeln('Time vencedor: ', n2);
writeln('Numero de gols: ', t2)
end
else
writeln('EMPATE. Nao houve vencedor.');
readln();

END.
