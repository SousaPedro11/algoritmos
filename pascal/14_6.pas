{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program quatorze_seis;
var
l: array [1..10] of string;
nome: string;
i: integer;
match: boolean;

begin
writeln('Este programa armazena o nome de 10 convidados num vetor e verifica se as pessoas na recepcao estao na lista ou nao.');
writeln();

for i:=1 to 10 do
begin
writeln('Informe o nome do convidado ',i);readln(l[i]);
end;

writeln();
writeln('RECEPCAO');
writeln('Informe o nome da pessoa na recepcao para verificar se esta na lista');readln(nome);

match:=False;
for i:= 1 to 10 do
begin
if nome=l[i] then match:=True;
end;

if (match) then
writeln('Acesso permitido. Bem vindo!')
else
writeln('Seu nome nao consta na lista de convidados. Acesso negado.');

readln();
end.
