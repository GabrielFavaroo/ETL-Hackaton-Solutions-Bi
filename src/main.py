import tabula
import pandas as pd
#sequencia de tabelas = 10-11,12-13,14-28,29-38,39-55,56-71,72-85
tabela1 = tabula.read_pdf(
    "data\raw\eOuve - Limeira.pdf",
      pages="10-11",
      #stream=True, #gerou inumeras ocorrencias de NaN (not a number)
        lattice=True,#demonstrou melhor resultado em ler por conta de ser feito para tabelas com grade visivel
        multiple_tables=False,
      encoding = "latin1"
      
      
      );

tabela2 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="12-13",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );


tabela3 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="14-28",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );


tabela4 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="29-38",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );

tabela5 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="39-55",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );

tabela6 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="56-71",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );


tabela7 = tabula.read_pdf(
    "eOuve - Limeira.pdf",
      pages="72-85",
        lattice=True,
        multiple_tables=False,
      encoding = "latin1"
      
      
      );



colunasAssuntosSituacao = ['Assunto',	'Aberto',	'Agendado',	'Cancelado',	'Concluído'	,'Em andamento',	'Pendente',	'Total']
colunasSecretariaSituacao = ['Secretaria',	'Aberto',	'Agendado',	'Cancelado',	'Concluído', 'Em andamento',	'Pendente',	'Total']
colunasSecretariaTipo = ['Secretaria','Denúncia',	'Doação',	'Elogio',	'Informação',	'Reclamação',	'Simplifique'	,'Solicitação',	'Sugestão',	'Total']
colunasAssuntosTipo = ['Assunto','Denúncia',	'Doação',	'Elogio',	'Informação',	'Reclamação',	'Simplifique'	,'Solicitação',	'Sugestão',	'Total']
colunasBairroTipo = ['Bairro','Denúncia',	'Doação',	'Elogio',	'Informação',	'Reclamação',	'Simplifique'	,'Solicitação',	'Sugestão',	'Total']
colunasBairroSituacao = ['Bairro',	'Aberto',	'Agendado',	'Cancelado',	'Concluído', 'Em andamento',	'Pendente',	'Total']

modeloSituacao = ['Aberto',	'Agendado',	'Cancelado',	'Concluído'	,'Em andamento',	'Pendente',	'Total']
modeloTipo = ['Denúncia',	'Doação',	'Elogio',	'Informação',	'Reclamação',	'Simplifique'	,'Solicitação',	'Sugestão',	'Total']

valoresSituacao = {'Aberto' : int,	'Agendado' : int,	'Cancelado': int,	'Concluído': int	,'Em andamento': int,	'Pendente': int,'Total' : int}
valoresTipo = {'Denúncia': int,	'Doação': int,	'Elogio': int,	'Informação': int,	'Reclamação': int,	'Simplifique': int	,'Solicitação': int,	'Sugestão': int,'Total' : int}






def limparTexto(tabela,coluna):
    tabela[coluna] = tabela[coluna].str.replace('\r',' ',regex = False)

    return tabela
    


def limparValores(tabela,listaDeColunas):
    for coluna in listaDeColunas:
        tabela[coluna] = tabela[coluna].astype(str).str.replace('.','',regex = False).str.replace(',','.',regex = False)
        tabela[coluna] = pd.to_numeric(tabela[coluna], errors='coerce')
        tabela[coluna] = tabela[coluna].fillna(0).astype('Int64')

    return tabela

#para evitar a criacao de outra lista de colunas sem o parametro Total, o metodo abaixo tem a variavel colunasParaSomar que recebe todas as colunas -1 que é a Total
def calcularTotal(tabela,modeloColunas):
    colunasParaSomar = modeloColunas[:-1]
    tabela['Total'] = tabela[colunasParaSomar].sum(axis=1)
    return tabela




tabela1[0].columns = colunasSecretariaTipo
tabela2[0].columns = colunasSecretariaSituacao
tabela3[0].columns = colunasAssuntosTipo
tabela4[0].columns = colunasAssuntosSituacao
tabela5[0].columns = colunasBairroTipo
tabela6[0].columns = colunasBairroSituacao
tabela7[0].columns = colunasSecretariaTipo


#apagar ultima linha
tabela1[0].drop(tabela1[0].tail(1).index,inplace=True)
tabela2[0].drop(tabela2[0].tail(1).index,inplace=True)
tabela3[0].drop(tabela3[0].tail(1).index,inplace=True)
tabela4[0].drop(tabela4[0].tail(1).index,inplace=True)
tabela5[0].drop(tabela5[0].tail(1).index,inplace=True)
tabela6[0].drop(tabela6[0].tail(1).index,inplace=True)
tabela7[0].drop(tabela7[0].tail(1).index,inplace=True)


tabela1[0] = limparValores(tabela1[0],modeloTipo)
tabela2[0] = limparValores(tabela2[0],modeloSituacao)
tabela3[0] = limparValores(tabela3[0],modeloTipo)
tabela4[0] = limparValores(tabela4[0],modeloSituacao)
tabela5[0] = limparValores(tabela5[0],modeloTipo)
tabela6[0] = limparValores(tabela6[0],modeloSituacao)
tabela7[0] = limparValores(tabela7[0],modeloTipo)


tabela1[0] = calcularTotal(tabela1[0],modeloTipo)
tabela2[0] = calcularTotal(tabela2[0],modeloSituacao)
tabela3[0] = calcularTotal(tabela3[0],modeloTipo)
tabela4[0] = calcularTotal(tabela4[0],modeloSituacao)
tabela5[0] = calcularTotal(tabela5[0],modeloTipo)
tabela6[0] = calcularTotal(tabela6[0],modeloSituacao)
tabela7[0] = calcularTotal(tabela7[0],modeloTipo)



tabela1[0] = limparTexto(tabela1[0],'Secretaria')
tabela2[0] = limparTexto(tabela2[0],'Secretaria')
tabela3[0] = limparTexto(tabela3[0],'Assunto')
tabela4[0] = limparTexto(tabela4[0],'Assunto')
tabela5[0] = limparTexto(tabela5[0],'Bairro')
tabela6[0] = limparTexto(tabela6[0],'Bairro')
tabela7[0] = limparTexto(tabela7[0],'Secretaria')

#o codigo abaixo indica que praticamente todo o conteudo foi lido como String(object)
#display(tabela1[0].dtypes)
#display(tabela2[0].dtypes) 
#display(tabela3[0].dtypes) 
#display(tabela4[0].dtypes) 
#display(tabela5[0].dtypes) 
#display(tabela6[0].dtypes) 
#display(tabela7[0].dtypes) 


listaDeTabelas = [tabela1[0],tabela2[0],tabela3[0],tabela4[0],tabela5[0],tabela6[0],tabela7[0]]

def tabelasParaCsv(listacomTabelas):
    n = 1
    for tabela in listacomTabelas:
        tabela.to_csv(f'Tabela{n}_TratadaHackaton.csv',mode = 'w',index = False, header = True)
        n = n + 1

tabelasParaCsv(listaDeTabelas)

display(tabela1[0])
display(tabela2[0])
display(tabela3[0])
display(tabela4[0])
display(tabela5[0])
display(tabela6[0])
display(tabela7[0])


