program constante_variavel;

        CONST // declaração de constantes
        PI = 3.1415926;

VAR
idade:INTEGER; //inteiro
salario:REAL; //real
sexo:CHAR; //caractere
nome:STRING; //vários caracteres
//lógico=booleano
aprovado,reprovado:BOOLEAN;

begin
idade:=24;
salario:=1500;
sexo:='M';
nome:='Pedro Sousa';
aprovado:=true;
reprovado:=false;

writeln('O valor de PI ',chr(130),' =',PI);
writeln('Minha idade ',chr(130),' = ', idade);
writeln('Meu salario =',salario);
writeln('Sexo = ',sexo);
writeln('Meu nome = ',nome);
writeln('Aprovado = ',aprovado, ' -----> Reprovado = ',reprovado);

readln;

end.
