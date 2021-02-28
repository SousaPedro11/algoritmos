{Universidade Federal do Para
Instituto de Ciencias Eaxatas e Naturais
Faculdade de Computacao - Bacharelado em Sistemas de Informacao
Disciplina: Algoritmos
Profa.: Marcelle Mota
Estudantes: Pedro Paulo L Sousa; Jhonata Natividade
}

program agenda_fone;
uses
Crt,sysutils;   //controla saida no cmd e utilitarios de sistema

type                      //define registro
reg_agenda = record
nome: string;
celular: longint;
end;

arq_agenda = file of reg_agenda;     //define arquivo de registro

var
//contato: array [1..9999] of reg_agenda;
i:integer;
reg_a:reg_agenda;
arq_a:arq_agenda;
opcao:char;
caminho,usuario{,arquivoexterno}:string;


begin
{writeln('Este programa cria um arquivo de agenda telefonica com nome e celular.');
write('Digite um nome para o arquivo a ser criado: ');readln(arquivoexterno);
caminho:= 'C:\\Users\\201711140038\\Desktop\\'+ arquivoexterno;} //<-outra forma


//define sistema operacional
  {$IFDEF Linux}
  usuario:=GetUserDir; //retorna a pasta home
  caminho := usuario + 'agenda';
  {$ELSE}
  usuario:='C:\\Users\\'+ GetEnvironmentVariable('USERNAME')+'\\Desktop\\'; //getenv... nome usuario
  caminho:= usuario+'agenda';
  {$ENDIF}

assign(arq_a,caminho);   //abre arquivo
rewrite(arq_a);          //define arquivo como leitura e escrita
opcao:='s';              //inicializa opcao
i:=0;
while (opcao='s') or (opcao=#13) do   //enquanto opcao igual a s ou enter, faca
begin
i:=i+1;   //contador
clrscr;   //limpa a tela
gotoxy(1,1);     //move o cursor para o ponto
     writeln('Este programa cria um arquivo de agenda telefonica com nome e celular.');
     writeln('CONTATO ',i);
     write('Informe o nome: ');readln(reg_a.nome);    //le nome para o registro
     while length(reg_a.nome)=0 do    //enquanto tamanho do nome for 0, faca
     begin
     write('Este campo nao deve "ficar em branco". Informe o nome: ');readln(reg_a.nome);
     end;
     write('Informe o numero de celular: ');readln(reg_a.celular);   //le celular para o registro
     write(arq_a,reg_a);   //escreve o registro no arquivo
     write('Deseja fazer outra operacao?(S/n) ');opcao:=ReadKey;writeln(opcao);    //le opcao
     Delay(250);
     writeln();

                   while (opcao<>'s') and (opcao<>'n') and (opcao<>#13) do   //controle opcao
                   begin
                   write('Opcao invalida! Deseja fazer outra operacao?(S/n) ');opcao:=Readkey;writeln(opcao);
                   Delay(250);
                   writeln();
                   end;
                   if opcao='n' then writeln('Fim do Programa');
end;
writeln();
writeln('O arquivo "agenda" encontra-se em: ',usuario);  //mostra caminho
writeln();
write('<Tecle algo para continuar>');readln();
end.
