{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}
program calc;
uses
Crt;

var
option,key:char;

procedure adicao;
var
z,a,b: real;

begin
writeln('Procedimento de Adicao');
writeln();
writeln('Informe o valor de A');readln(a);
writeln('Informe o valor de B');readln(b);
z:=a+b;
writeln();
writeln('Soma de ',a:0:2,' e ',b:0:2,': ',z:0:2);
end;

procedure subtracao;
var
z,a,b: real;

begin
writeln('Procedimento de Subtracao');
writeln();
writeln('Informe o valor de A');readln(a);
writeln('Informe o valor de B');readln(b);
z:=a-b;
writeln();
writeln('Subtracao de ',a:0:2,' e ',b:0:2,': ',z:0:2);
end;

procedure multiplicacao;
var
z,a,b: real;

begin
writeln('Procedimento de Multiplicacao');
writeln();
writeln('Informe o valor de A');readln(a);
writeln('Informe o valor de B');readln(b);
z:=a*b;
writeln();
writeln('Multiplicacao de ',a:0:2,' e ',b:0:2,': ',z:0:2);
end;

procedure divisao;
var
z,a,b: real;

begin
writeln('Procedimento de Divisao');
writeln();
writeln('Informe o valor de A');readln(a);
writeln('Informe o valor de B');readln(b);
writeln();
while b=0 do
begin
writeln('O divisor nao pode ser igual a zero. Informe outro valor');readln(b);
writeln();
end;
z:=a/b;
writeln('Divisao de ',a:0:2,' e ',b:0:2,': ',z:0:2);
end;

begin
option:='s';
while option<>'n' do
begin
clrscr;
gotoxy(9,2);writeln('Menu Principal');
writeln('Escolha uma da operacoes a fazer');
writeln('1 - Soma');
writeln('2 - Subtracao');
writeln('3 - Multiplicacao');
writeln('4 - Divisao');
//writeln('e - encerrar');
writeln();
write('Opcao: ');readln(option);
{while (option<'1') or (option>'4') or (option<>'e') do
begin
writeln('Opcao invalida! Escolha uma opcao de 1 a 4.');readln(option);
end;
}
writeln();
case option of
'1': adicao;
'2': subtracao;
'3': multiplicacao;
'4': divisao;
end;
writeln();
if (option>='1') and (option<='4') then
begin
write('Deseja fazer outra operacao?(S/n)');readln(key);
while (key<>'s') and (key<>'n') and (key<>#13) do
begin
write('Opcao invalida! Deseja fazer outra operacao?(S/n)');readln(key);
option:=key;
end;
end
else if option='n' then
writeln('Fim do Programa')
else
begin
writeln('Opcao Invalida. Escolha de acordo com o Menu Principal.');
write('<Tecle algo para continuar>');readln();
end;

writeln();
if key='n' then
begin
writeln();
option:=key;
writeln('Fim do Programa');
end;

end;
readln();
end.
