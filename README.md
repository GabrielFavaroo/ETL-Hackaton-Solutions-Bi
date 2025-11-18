🏆 HACKATHON SOLUTIONS BI 2025: PIPELINE ETL - CIDADANIA ATIVA
🎯 Propósito do Projeto: Transformando Dados Brutos em Insights EstratégicosEste projeto foi desenvolvido como uma solução de Business Intelligence (BI) para o Hackathon Solutions BI 2025. 
Nosso objetivo principal é democratizar o acesso aos dados de ouvidoria de Limeira (eOuve) extraídos do relatório PDF, transformando informações complexas e inacessíveis em um formato estruturado (CSV) pronto para análise estratégica.Ao criar um pipeline ETL robusto, garantimos que gestores e analistas possam rapidamente:Identificar gargalos no atendimento da prefeitura por Secretaria, Assunto e Bairro.Mensurar a performance de resposta e resolução das solicitações.Gerar dashboards e relatórios para guiar a tomada de decisão focada na melhoria da Cidadania Ativa e na eficiência do serviço público.

2. ⚙️ Estrutura e TecnologiaO projeto segue a arquitetura de boas práticas de Engenharia de Dados, separando as responsabilidades (E, T, L) e garantindo um código modular e manutenível.ComponentePastaResponsabilidadeTecnologias ChaveCódigo Fontesrc/Contém a lógica de extração, limpeza e orquestração do pipeline.Python, pandasDados Brutosdata/raw/Armazena o PDF original, intocado.PDF (Input)Resultadosdata/processed/Armazena os DataFrames limpos, prontos para BI.CSV (Output)Análisenotebooks/(Opcional) Ambiente para validação e exploração inicial dos dados.Jupyter

3. 🛠️ Tecnologias e DependênciasPara executar este projeto, você precisa do ambiente Python configurado.FerramentaUsoInstalação (Exemplo)Python (3.x)Linguagem de programação principal.Instalado via Anaconda/Miniconda.PandasTransformação de dados (limpeza, cálculo de totais, tipagem).pip install pandasTabula-pyExtração de tabelas do PDF (Essencial para a etapa E).pip install tabula-pyJupyterAmbiente de desenvolvimento interativo e análise exploratória.conda install jupyter🔑
   IMPORTANTE: Todas as dependências do projeto são listadas no arquivo requirements.txt.Instalação Rápida (Recomendada via ambiente virtual)Bash# 1. Crie um ambiente virtual (venv)
python -m venv venv

Ative o ambiente
source venv/bin/activate  # Linux/macOS  ||   # venv\Scripts\activate   # Windows


Instale todas as dependências
pip install -r requirements.txt

4. ▶️ Guia de Execução
Siga estes passos para rodar o pipeline ETL e gerar os arquivos de saída:Posicione o PDF: Certifique-se de que o arquivo de entrada (eOuve - Limeira.pdf) esteja na pasta data/raw/.Ative o Ambiente: Garanta que seu ambiente virtual esteja ativado (ver seção 3).Execute o Orquestrador: A partir da raiz do projeto (etl-project/), execute o script principal.Bashpython src/main.py

6. 📤 Saída Esperada (Output)Após a execução, os DataFrames processados estarão disponíveis como arquivos CSV tipados e limpos na pasta:data/processed/
├── Tabela1_TratadaHackaton.csv
├── Tabela2_TratadaHackaton.csv
└── ... (Tabela7_TratadaHackaton.csv)
Esses arquivos estão prontos para serem carregados em um banco de dados ou diretamente em uma ferramenta de BI, como o Power BI ou Tableau, para a criação dos dashboards finais do Hackathon.
