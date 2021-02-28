Program torreHanoi;
var
n,t,count_n:integer;

 procedure hanoi(n:integer;a,b,c:char);
 {mova n discos do pino a para o pino c usando o pino b como auxiliar}
 begin
   if n=1
   then
   begin
   count_n:=count_n+1;
   writeln(count_n,' - mova o disco ',n,' do pino ',a,' para o pino ',b)
   end
   else
   begin
     hanoi(n-1,a,c,b);
        count_n:=count_n+1;
     writeln(count_n,' - mova o disco ',n,' do pino ',a,' para o pino ',b);
     hanoi(n-1,c,b,a);
   end;
 end;

 procedure teste0(n:integer);
 begin
  while n=0 do
   begin
    writeln('SAIDA');
    writeln('Digite um valor valido para o numero de discos. Maior de 0.');
    writeln();
    writeln('ENTRADA');
    writeln('Escolha o numero de discos para a Torre de Hanoi');
    read(t);
    n:=t;
    writeln();
   end;
 end;

begin
 writeln('ENTRADA');
 count_n:=0;
 writeln('Escolha o numero de discos para a Torre de Hanoi');
 readln(n);
 writeln();
 teste0(n);
if t<>0 then n:=t;

 writeln('SAIDA'); 
 writeln('Numero de discos = ',n);
 writeln('Numero minimo de movimentos: ',round(exp(n*ln(2)))-1,'.');
 writeln('Para resolver a Torre com ',n,' discos. Faca os seguintes movimentos:');
 hanoi(n,'A','C','B'); writeln('Fim de programa'); readln();
end.
