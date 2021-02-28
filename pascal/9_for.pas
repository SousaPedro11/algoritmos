{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program nove_for;

var
i,v:integer;//i - contador(de 1 a 10); v - valor de entrada

BEGIN
writeln('Este programa faz a tabuada (da multiplicacao) de um numero.');
writeln('Digite o numero para fazer sua tabuada (numero que multiplica de 1 a 10).');readln(v);

i:=1;
writeln();
writeln('TABUADA DO ', v);
for i:= 1 to 10 do//faz operacoes com i de 1 ate 10
begin
writeln(v,' x ',i,' = ', v*i);//multiplica e mostra na tela
end;
readln();	
	
END.

