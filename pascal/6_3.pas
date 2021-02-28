{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program seis_tres;

var
num1, num2: real;//declara variaveis

begin
//entrada
writeln('Este programa calucula as operacoes basicas entre dois numeros.');
writeln('Digite um valor para o primeiro numero'); readln(num1);
writeln('Digite um valor para o segundo numero'); readln(num2);

//saida
writeln();
writeln('Operacoes entre ',num1:0:2,' e ',num2:0:2,':');
writeln('Soma ---> ',num1+num2:0:2);
writeln('Subtracao ---> ',num1-num2:0:2);
writeln('Multiplicacao ---> ',num1*num2:0:2);
writeln('Divisao ---> ',num1/num2:0:2);
readln();
end.
