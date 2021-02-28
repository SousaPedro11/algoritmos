{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_nove;

const
usert=1234;
passt=9999;

var
user,pass:integer;

begin
writeln('Este programa simula um login.');
writeln('Para isso, deve-se informar usuario e senha (ambos numericos).');

writeln();
writeln('Insira seu codigo de usuario.');readln(user);
if user<>usert then
writeln('USUARIO INVALIDO!')
else
begin
writeln('Insira sua senha');readln(pass);
if pass<>passt then
writeln('SENHA INCORRETA!')
else
writeln('ACESSO PERMITIDO');
end;

end.
