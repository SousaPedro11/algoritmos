{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program onze_um;

var
veta,vetb: array[1..10] of integer;   //declara vetor a e vetor b como vetores de inteiros
i,j: integer;  //declara contadores inteiros

BEGIN
writeln('Este programa calcula a soma entre dois vetores de 10 posicoes');	//imprime mensagem

for j:= 1 to 2 do  //contador de selecao dos vetores
begin
for	i:= 1 to 10 do  //contador das posicoes dos vetores
        begin
        if j=1 then  //condicao para selecao dos vetores
           begin
           writeln('Informe a posicao ',i,' do vetor A');
           readln(veta[i]);  //recebe valor na posicao i do vetor A
           end
        else
           begin
           writeln('Informe a posicao ',i,' do vetor B');
           readln(vetb[i]);  //recebe valor na posicao i do vetor B
           end;
        end;
writeln();
end;

//SAIDA
for j:=1 to 3 do  //contador selecao de vetores
begin
if j=1 then  //condicao nome vetor A
write('Vetor A = [ ')
else if j=2 then //condicao nome vetor B
     write('Vetor B = [ ')
     else
     write('Vetor SOMA = [ ');  //nome vetor soma
for i:=1 to 10 do   //contador posicao vetores
    begin
    if j=1 then    //condicao selecao vetor A
       write(veta[i],' ')   //escreve posicao i do vetor A
    else if j=2 then
       write(vetb[i],' ')   //escreve posicao i do vetor B
       else
       write(veta[i]+vetb[i],' ');  //escreve posicao i do vetor SOMA
    end;
writeln(']');
end;

readln();
END.
