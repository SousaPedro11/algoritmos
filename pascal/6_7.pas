{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_sete;

var//declara variaveis
a,b,tempor:integer;

begin
//entrada
writeln('Este programa inverte dois valores inteiros e mostra o maior.');
writeln('Digite o valor de A.');readln(a);
writeln('Digite o valor de B.');readln(b);
//imprime atual
writeln('A ---> ',a);
writeln('B ---> ',b);
 writeln();
//troca variavel
tempor:=a;
a:=b;
b:=tempor;
//imprime novo
writeln('A agora vale ---> ', a);
writeln('B agora vale ---> ', b);
//imprime maior
if a>b then
writeln('O maior valor entre eles ---> ', a)
else
writeln('O maior valor entre eles ---> ', b);

readln();
end.
