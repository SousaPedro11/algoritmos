{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program onze_dois;

var
a: array[1..100] of integer;  //declara vetor de inteiros com 100 posicoes
i: integer;   //declara contador inteiro

begin
writeln('Este programa preenche um vetor de 100 posicoes com 0 na posicao impar e 1 na par.');
writeln();
writeln('Vetor(posicao) = valor');

for i:= 1 to 100 do //contador posicao i do vetor a
begin
if (i mod 2) <> 0 then  //condicao posicao impar
a[i]:=0
else //posicao par
a[i]:=1;

writeln('a(',i,') = ',a[i]);  //escreve posicao i do vetor
end;

readln();
end.
