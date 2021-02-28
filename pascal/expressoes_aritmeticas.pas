program expressoes_aritmeticas;

VAR
A,B,C:INTEGER; //VARIAVEIS INTEIRAS
D:REAL;        //VARIAVEIS REAIS

begin
A:=5;
B:=10;
C:=-8;
D:=1.5;

writeln('Considere 5, 10, -8 e 1.5 os respectivos valores de A, B, C e D. Com isso temos:');
writeln('a) 2 * A mod 3 - C = ',2*(A)MOD(3)-C);
writeln('b) rad(-2*C)div 4 = ',round(SQRT(-2*C))DIV(4));//round() arredonda para o inteiro mais proximo, trunc arredonda pro mais baixo.
writeln('c) ((20 div 3) div 3) + pot(8,2)/2 = ',(((20)div(3))div(3)+round(sqr(8)/2)));
writeln('d) (30 mod 4 * pot(3,3)) * -1 = ',((30)mod(4)*round(exp(3*ln(3))))*(-1));//exp(x*ln(y))=y^x=pot(y,x).
writeln('e) pot(-C,2)+(D*10)/A = ',sqr(-C)+(D*10)/A); //deixei resultado real devido D ser real
writeln('f) rad(pot(A,B/A))+C*D = ',sqrt(exp((B/A)*ln(A)))+C*D);//O mesmo da questao e).
readln();

end.
