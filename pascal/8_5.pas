{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_cinco;
var
n1,n2,media:real;
conc:string;

begin
writeln('Este programa calcula a media de um aluno baseado em duas avaliacoes');
writeln('Insira a nota da primeira avaliacao');readln(n1);
while (n1 < 0) or (n1>10) do
begin
writeln('Digite um valor valido para a nota (de 0 a 10)!');
writeln('Insira a nota da primeira avaliacao');readln(n1);
end;

writeln('Insira a nota da segunda avaliacao');readln(n2);
while (n2 < 0) or (n2>10) do
begin
writeln('Digite um valor valido para a nota (de 0 a 10)!');
writeln('Insira a nota da segunda avaliacao');readln(n2);
end;

media:=(n1+n2)/2;
if media < 5 then
begin
writeln();
writeln('Reprovado! Estude mais!');
writeln('Media= ', media:0:2)
end
else
begin
writeln('Aprovado! Parabens!');
writeln('Media= ', media:0:2);
if (media>=5)and(media<7) then
conc:='REGULAR'
else
if (media>=7)and(media<9) then
conc:='BOM'
else
conc:='EXCELENTE';
writeln('Conceito= ' ,conc);

end;
readln();

end.
