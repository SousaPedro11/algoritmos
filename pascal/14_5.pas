{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_cinco;
var
atl: array [1..5] of real;
soma, media: real;
i: integer;

begin
writeln('Este programa recebe a altura de 5 atletas, calcula a media e mostra quais estao acima dela.');

soma:=0;
for i:= 1 to 5 do
begin
writeln('Informe a altura do atleta ',i);readln(atl[i]);
while (atl[i]<0.5) or (atl[i]>3) do
begin
writeln('Valor invalido! Informe a altura do atleta ',i,' (de 0.5 a 3m)');readln(atl[i]);
end;
soma:=soma+atl[i];
end;

media:=soma/5;

writeln();
writeln('Media das Alturas: ',media:0:2,'m');
writeln('Atletas com altura acima da media:');
for i:= 1 to 5 do
begin
if atl[i]>media then writeln('Atleta ',i,' = ',atl[i]:0:2,'m');
end;
readln();
end.
