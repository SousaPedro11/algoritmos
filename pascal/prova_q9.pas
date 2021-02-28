{
UNIVERSIDADE FEDERAL DO PARA
INSTITUTO DE CIENCIAS EXATAS E NATURAIS
FACULDADE DE COMPUTACAO - CURSO DE BACHARELADO EM SISTEMAS DE INFORMACAO
DISCIPLINA: ALGORITMOS
PROFA: MARCELLE MOTA
ESTUDANTE: PEDRO PAULO LISBOA DE SOUSA / 201711140038
}

program prova_q9;
var
conv:array[1..10] of string;//declara conv como vetor de 10 posicoes de string, vetor convidados
recep:string; //declara recep como string, nome na recepcao
i:integer;  //contador
match:boolean; //se v, consta na lista; se f, nao consta

begin
writeln('Este programa confere se as pessoas na recepcao estao na lista de convidados.');
writeln();

//le lista de convidados
writeln('Componha a lista de convidados.');
for i:= 1 to 10 do
begin
writeln('Insira o nome do convidado ',i);readln(conv[i]);
end;

writeln();

//le nome na recepcao
writeln('Confere recepcao');
writeln('Informe o nome da pessoa na recepcao.');readln(recep);

//procura nome da recepcao na lista de convidados
match:=False;
i:=0;
repeat
begin
i:=i+1;
if recep=conv[i] then match:=True;
end;
until (i=10) or (match); //repete ate i=10 ou match=true(esta na lista)

writeln();

//resultado da busca
write('RESULTADO: ');
if match then
writeln('Convidado consta na lista. Acesso permitido.')
else
writeln('Convidado nao consta na lista. Acesso negado.');

readln();
end.
