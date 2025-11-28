<div align="center">

<h1 style="font-size:40px; margin-bottom:10px;">🚀 Hackathon Solutions BI 2025</h1>
<h2 style="font-size:24px; color:#4CAF50; margin-top:0;">Pipeline ETL – Extração, Transformação e Limpeza de Dados do eOuve (Limeira)</h2>

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Library-Tabula-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Pandas-DataFrame-yellow?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completo-green?style=for-the-badge">

</div>

<hr>

<h2>📌 Sobre o Projeto</h2>

<p style="font-size:16px; line-height:1.6;">
Este projeto foi desenvolvido para o <b>Hackathon Solutions BI 2025</b>, com o objetivo de construir um pipeline completo de <b>ETL</b> para extração, saneamento e padronização dos dados do sistema <b>eOuve – Limeira</b>.  
A fonte original consiste em um relatório em PDF estruturado, exigindo técnicas robustas de parsing, limpeza textual, normalização e conversão para formatos analisáveis (CSV).
</p>

<hr>

<h2>🎯 Objetivos</h2>
<ul style="font-size:16px; line-height:1.8;">
  <li>Extrair múltiplas tabelas de um PDF com intervalos de páginas distintos utilizando <b>Tabula</b>.</li>
  <li>Realizar limpeza textual avançada (acentos, caracteres especiais, espaços duplicados, normalização Unicode).</li>
  <li>Padronizar nomes de colunas e valores numéricos.</li>
  <li>Recalcular colunas de totais a partir de campos originais.</li>
  <li>Gerar 7 tabelas tratadas em CSV, prontas para análise em BI.</li>
</ul>

<hr>

<h2>🧩 Arquitetura do Pipeline</h2>

<pre style="background:#1e1e1e; color:#fff; padding:18px; border-radius:8px; font-size:14px;">
📄 PDF Original (eOuve - Limeira.pdf)
           │
           ▼
🔍 Extração das Tabelas (Tabula + Python)
           │
           ▼
🧼 Limpeza e Normalização:
    - Remoção de acentos (unicodedata)
    - Remoção de caracteres especiais (regex)
    - Nomes de colunas padronizados (snake_case)
    - Conversão numérica segura (to_numeric)
    - Recalculo de totais
           │
           ▼
📊 Geração das Tabelas Finais:
    ✔ Tabela 1 – Tipo por Secretaria
    ✔ Tabela 2 – Situação por Secretaria
    ✔ Tabela 3 – Tipo por Assunto
    ✔ Tabela 4 – Situação por Assunto
    ✔ Tabela 5 – Tipo por Bairro
    ✔ Tabela 6 – Situação por Bairro
    ✔ Tabela 7 – Tipo por Secretaria (Consolidada)
           │
           ▼
📁 Exportação em CSV (Tabelas Tratadas)
</pre>

<hr>

<h2>🛠 Tecnologias Utilizadas</h2>

<table style="width:100%; font-size:16px;">
  <tr>
    <td>🐍 Python 3.10</td>
    <td>📦 Pandas</td>
    <td>📑 Tabula (PDF Parsing)</td>
  </tr>
  <tr>
    <td>🔤 unicodedata</td>
    <td>🧹 Regex</td>
    <td>📁 pathlib (com caminhos relativos)</td>
  </tr>
</table>

<hr>

<h2>📥 Estrutura de Pastas</h2>

<pre style="background:#1e1e1e; color:#fff; padding:18px; border-radius:8px; font-size:14px;">
Hackaton Solutions BI/
│
├── data/
│   └── raw/
│       └── eOuve - Limeira.pdf   ← Arquivo de origem
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── ETL Hackaton Solutions BI.ipynb
│
└── output/
    ├── Tabela1_TratadaHackaton.csv
    ├── Tabela2_TratadaHackaton.csv
    ├── ...
    └── Tabela7_TratadaHackaton.csv
</pre>

<hr>

<h2>📌 Principais Recursos do Código</h2>

<h3>✔ Extração de múltiplas tabelas</h3>
<p>O script percorre sequências de páginas específicas:</p>
<pre style="background:#272822; color:#f8f8f2; padding:16px; border-radius:8px;">
sequenciaDeTabelas = ["10-11","12-13","14-28","29-38","39-55","56-71","72-85"]
</pre>

<h3>✔ Caminhos relativos com segurança total</h3>
<pre style="background:#272822; color:#f8f8f2; padding:16px; border-radius:8px;">
LocalNT = Path().resolve()
caminhoPDF = LocalNT.parent / "data" / "raw" / "eOuve - Limeira.pdf"
</pre>

<h3>✔ Limpeza textual aprimorada</h3>
<ul>
  <li>Normalização NFKD</li>
  <li>Remoção de acentos</li>
  <li>Eliminação de caracteres inválidos</li>
  <li>Padronização de espaços</li>
</ul>

<h3>✔ Padronização de colunas</h3>
<pre style="background:#272822; color:#f8f8f2; padding:16px; border-radius:8px;">
nomeLimpo = re.sub(r'[-–—\s/.]+','_',nomeColuna)
</pre>

<h3>✔ Conversão e soma de colunas numéricas</h3>
<pre style="background:#272822; color:#f8f8f2; padding:16px; border-radius:8px;">
tabela[coluna] = pd.to_numeric(tabela[coluna], errors='coerce')
</pre>

<hr>

<h2>📤 Saída Final</h2>

<p>O script gera automaticamente <b>7 arquivos CSV limpos e estruturados</b>, prontos para BI, dashboards e análises.</p>

<ul style="font-size:16px; line-height:1.8;">
  <li><b>Tabela1_TratadaHackaton.csv</b></li>
  <li><b>Tabela2_TratadaHackaton.csv</b></li>
  <li>...</li>
  <li><b>Tabela7_TratadaHackaton.csv</b></li>
</ul>

<hr>

<h2>📈 Exemplos Visuais</h2>

<p>Você pode adicionar aqui imagens de como os dados estavam e como ficaram:</p>

<ul>
  <li>📸 Antes – Tabela bruta do PDF</li>
  <li>📸 Depois – Tabela limpa e padronizada</li>
</ul>

<hr>

<h2>🚀 Como Executar</h2>

<pre style="background:#1e1e1e; color:#fff; padding:18px; border-radius:8px; font-size:14px;">
# 1. Instale as dependências
pip install pandas tabula-py

# 2. Coloque o PDF em: /data/raw/

# 3. Execute o script principal
python main.py
</pre>

<hr>

<h2>💡 Autor</h2>

<p style="font-size:16px;">
<b>Gabriel Favaro</b><br>
Desenvolvedor Back-end 
</p>

<hr>
