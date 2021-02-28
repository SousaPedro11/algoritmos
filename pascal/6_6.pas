{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_seis;

var//declara variaveis
nome:string;
nota1, nota2:real;
begin
//entrada nome
writeln('Este programa calcula a media entre 2 notas de um aluno.');
writeln();
writeln('Digite o nome do aluno.'); readln(nome);
//entrada nota 1
writeln('Digite a nota da primeira prova.'); readln(nota1);
//condicao nota
while (nota1<0) or (nota1>10) do
begin
writeln('O valor da nota deve ser >=0 ou <=10.');
writeln('Digite a nota da primeira prova.'); readln(nota1);
end;
//entrada nota 2
writeln('Digite a nota da segunda prova.'); readln(nota2);
//condicao nota
while (nota2<0) or (nota2>10) do
begin
writeln('O valor da nota deve ser >=0 ou <=10.');
writeln('Digite a nota da segunda prova.'); readln(nota2);
end;
//saida
writeln();
writeln('Estudante: ',nome);
writeln('Notas: ',nota1:0:2,' (P1), ',nota2:0:2,' (P2)');
writeln('Media: ', (nota1+nota2)/2:0:2);
readln();
end.
