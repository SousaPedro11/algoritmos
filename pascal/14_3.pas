{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_tres;
var
aluno: array [1..10] of real;
i: integer;
soma, media: real;

begin
writeln('Este programa recebe a nota de 10 alunos, calcula a media da turma e permite a consulta se esta abaixo ou acima da media.');
writeln();

soma:=0;
for i:= 1 to 10 do
begin
writeln('Informe a nota do aluno ',i);readln(aluno[i]);
while (aluno[i]<0)or(aluno[i]>10) do
	begin
	writeln('Nota invalida. Insira a nota do aluno ',i,' (de 0 a 10).');readln(aluno[i]);
	end;
soma:=soma+aluno[i];
end;

media:=soma/10;

writeln();
writeln('Qual aluno deseja consultar a nota?');readln(i);
while (i<0)or(i>10) do
	begin
	writeln('Aluno invalido. Qual aluno deseja consultar a nota? (de 0 a 10).');readln(i);
	end;
writeln();

writeln('Media da turma = ',media:0:2);
writeln('Nota do aluno ',i,' = ',aluno[i]:0:2);

if aluno[i]<media then
writeln('O aluno ',i,' esta abaixo da media da turma: ',aluno[i]-media:0:2,'pts')
	else if aluno[i]=media then
	writeln('O aluno ',i,' tem nota igual a media da turma.')
		else
		writeln('O aluno ',i,' esta acima da media da turma: ',aluno[i]-media:0:2,'pts');

readln();
end.
