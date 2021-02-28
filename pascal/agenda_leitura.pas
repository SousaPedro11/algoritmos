{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program agenda_fone;
uses
Crt,sysutils;

type
reg_agenda = record
nome: string;
celular: longint;
end;

arq_agenda = file of reg_agenda;

var
i:integer;
reg_a:reg_agenda;
arq_a:arq_agenda;
caminho,usuario:string;


begin
  {$IFDEF Linux}
  usuario:=GetUserDir;
  caminho := usuario + 'agenda';
  {$ELSE}
  usuario:='C:\\Users\\'+ GetEnvironmentVariable('USERNAME')+'\\Desktop\\';
  caminho:= usuario+'agenda';
  {$ENDIF}
assign(arq_a,caminho);
//ATE AQUI FOI A MESMA MERDA DO ALGORITMO DE ESCRITA

reset(arq_a);   //define arquivo como leitura
writeln('Este programa le e imprime os dados de agenda telefonica com nome e celular.');
for i:= 1 to (filesize(arq_a)) do   //fazer de 1 ate tamanho do arquivo (ultimo registro)
begin
writeln('CONTATO ',i);
read(arq_a,reg_a);    //le o registro i do arquivo
write('Nome:    ');
writeln(reg_a.nome);  //escreve nome
write('Celular: ');
writeln(reg_a.celular);  //escreve celular
writeln();
Delay(250);
end;
writeln();
writeln('O arquivo "agenda" encontra-se em: ',usuario);
writeln();
write('<Tecle algo para continuar>');readkey;
end.
