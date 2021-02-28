program cartao_ponto;
type dia=record
     InMan,OutMan,InTar,OutTar:integer;
     end;

type TotDia = record
     Atraso, Horas:integer;
     end;

type
V1 = array [1..31] of dia;
V2 = array [1..31] of TotDia;

var
cont, i, toth, totatr: integer;
cartao:V1;
TotalDias:V2;

procedure Entrada;
var
dia,a,b,c,d:integer;

begin
cont:=0;
writeln('dia = ');readln(dia);
while (dia>0)and(dia<32) do
begin
writeln('entradamanha');readln(a);
writeln('saidadamanha');readln(b);
writeln('entradatarde');readln(c);
writeln('saidatarde');readln(d);
cartao[dia].InMan:=a;
cartao[dia].OutMan:=b;
cartao[dia].InTar:=c;
cartao[dia].OutTar:=d;
cont:=cont+1;
writeln('dia = ');readln(dia);
end;

end;

procedure calculo

begin

end.
