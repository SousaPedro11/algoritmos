Program triangulo;

var
a,b,c:integer; //Declara variaveis

begin
writeln('Informe o valor do lado "a" do triangulo'); readln(a); //Le variavel a
writeln('Informe o valor do lado "b" do triangulo'); readln(b); //Le variavel b
writeln('Informe o valor do lado "c" do triangulo'); readln(c); //Le variavel c

if (a<(b+c)) and (b<(a+c)) and (c<(a+b)) then //Se cond1 e cond2 e con3 for true entao...
begin  //inicia os comandos do entao
     if (a=b) and (b=c) then  //if interno: se cond1 e cond2 for true entao...
     writeln('Triangulo Equilatero') //se if interno for true, escreve isso
     else   //senao passa adiante
         if (a=b) or (a=c) or (b=c) then
         writeln('Triangulo Isosceles')
         else
         writeln('Triangulo Escaleno')
end
else
writeln('Estes valores não formam um triangulo');

readln();
end.
