{
Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program oito_seis;
var
n1,n2,n3:integer;

begin
writeln('Este progama ordena os tres valores digitados');
writeln('Informe o primeiro valor');readln(n1);
writeln('Informe o segundo valor');readln(n2);
writeln('Informe o terceiro valor');readln(n3);

if (n1=n2)or(n1=n3)or(n2=n3) then
begin
writeln('Nao sao aceitos valores iguais!');
if (n1=n2) then writeln('Os valores 1 e 2 sao iguais. Nao pode!');
if (n1=n3) then writeln('Os valores 1 e 3 sao iguais. Nao pode!');
if (n3=n2) then writeln('Os valores 2 e 3 sao iguais. Nao pode!');
writeln('Tente outra vez');
end
else
begin
if n3>n1 then
          begin
           if n1>n2 then write ('Ordem crescente --> ',n2,' ',n1,' ',n3)
                  else if n2<n3 then write('Ordem crescente --> ',n1,' ',n2,' ',n3);
          end;
if n1>n2 then
          begin
           if n2>n3 then write ('Ordem crescente --> ',n3,' ',n2,' ',n1)
                  else if n3<n1 then write('Ordem crescente --> ',n2,' ',n3,' ',n1);
          end;
if n1<n2 then
          begin
           if n3<n1 then write ('Ordem crescente --> ',n3,' ',n1,' ',n2)
                  else if n3<n2 then write('Ordem crescente --> ',n1,' ',n3,' ',n2);
          end;
end;
readln();
end.
