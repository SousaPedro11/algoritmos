{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program seis_nove;

var
idade:integer;//declara

begin
writeln('Este programa classifica o nadador de acordo com a idade:');
writeln('Idade         Categoria');
writeln('05-10          Infantil');
writeln('11-17          Juvenil');
writeln('18-35          Adulto');
writeln('36-            Senior');

writeln();
//entrada
writeln('Informe a idade do nadador.');readln(idade);
//condicao entrada
while (idade<5) or (idade >120) do
begin
if idade<5
then
writeln('Informe a idade de acordo com a classificacao (a partir de 5).')
else
writeln('Uau! +120! Pode ser perigoso para voce, melhor nao. Proximo...');
writeln('Informe a idade do nadador.');readln(idade);
end;
//saida
writeln();
writeln('Idade: ',idade);

case idade of
5..10: writeln('Voce pertence a categoria Infantil.');
11..17: writeln('Voce pertence a categoria Juvenil.');
18..35: writeln('Voce pertence a categoria Adulto.');
else
writeln('Voce pertence a categoria Senior.');
end;
readln();
end.
