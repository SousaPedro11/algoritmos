{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program dezesseis;

type
reg_a = record     //declara registro
nota: array [1..3] of real; //declara vetor de reais com 3 posicoes
media: real;  //declara media como real
nome: string;  //declara nome como string
end;

CONST //declara constante
n=10;  //numero de alunos

var
aluno: array [1..10] of reg_a;  //declara aluno como vetor de registro com 10 posicoes
i,j:integer;   //declara contadores inteiros
soma: real;   //declara soma como real

begin
writeln('Este programa cria um registro de 10 alunos com nome, notas e media final.');
writeln();

//SetLength(aluno,n+1);  //Funciona no compilador geany(linux)

for j:= 1 to n do   //contador para numero de alunos
begin
writeln('Insira o nome do aluno ',j);readln(aluno[j].nome);
soma:=0;   //inicializa soma
        for i:= 1 to 3 do  //contador notas
        begin
        writeln('Insira a nota ',i);readln(aluno[j].nota[i]);
        	while (aluno[j].nota[i]<0)or(aluno[j].nota[i]>10) do //critica (notas de 0 a 10)
        	begin
        	writeln('Nota invalida. Insira a nota ',i,' (de 0 a 10).');readln(aluno[j].nota[i]);
        	end;
        soma:=soma+aluno[j].nota[i]; //soma notas
        end;

aluno[j].media:=soma/3; //calcula media do aluno j
writeln();
end;

for j:=1 to n do  //contador dos 10 alunos
begin
writeln('ALUNO ',j);  //identifica aluno j
writeln('Nome = ',aluno[j].nome); //escreve nome do aluno j
               write('Notas = [ ');
               for i:= 1 to 3 do
               begin
                    write(aluno[j].nota[i]:0:2,' ');
               end;
               writeln(']');
writeln('Media = ',aluno[j].media:0:2); //escreve media do aluno j
writeln();
end;

readln();
end.
