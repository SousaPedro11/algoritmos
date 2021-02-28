{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_sete;
var
sal,parc:real;

begin
writeln('Este programa mostra se um banco pode conceder o emprestimo ao cliente ou nao.');
writeln('O emprestimo sera concedido se o valor das parcelas nao ultrapassar 30% do salario do cliente.');
writeln();
writeln('Informe o valor do salario do cliente');readln(sal);
while sal<=0 do
begin
writeln('Informe um valor valido para o salario (>0).');readln(sal);
end;

writeln('Informe o valor desejado para a parcela');readln(parc);
while parc<=0 do
begin
writeln('Informe um valor valido para a parcela (>0).');readln(parc);
end;

if parc>(sal*0.3) then
writeln('Emprestimo nao pode ser concedido')
else
writeln('Emprestimo sera concedido');
readln();
end.
