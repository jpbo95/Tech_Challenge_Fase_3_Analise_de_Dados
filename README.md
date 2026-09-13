# Tech Challenge - Fase 3

## Análise Exploratória do Mercado Brasileiro de Dados

### 1. Introdução

Neste projeto foi realizada uma análise exploratória do **mercado brasileiro de profissionais de Dados**, utilizando as pesquisas **State of Data Brasil** dos anos de 2023, 2024 e 2025.

O projeto integra conceitos de **Engenharia de Dados e Data Analytics**, desde a ingestão e tratamento dos dados até a consolidação, análise e geração de visualizações.

### 2. Objetivo

Desenvolver um fluxo de dados capaz de receber, tratar, consolidar e preparar as informações das diferentes edições da pesquisa State of Data Brasil.

A partir da base consolidada, foram analisados aspectos como:

* Perfil dos profissionais de Dados;
* Senioridade e experiência;
* Remuneração;
* Localização;
* Modelo de trabalho;
* Diversidade de gênero;
* Tecnologias utilizadas;
* Adoção de Inteligência Artificial.

### 3. Dataset

Foram utilizadas as pesquisas **State of Data Brasil**, realizadas pela comunidade **Data Hackers em parceria com a Bain**, considerando as edições de 2023, 2024 e 2025.

Os dados foram obtidos por meio das bases disponibilizadas no Kaggle.

Como as diferentes edições possuem alterações na estrutura e nomenclatura das perguntas e variáveis, foi necessário realizar um processo de **mapeamento e harmonização dos dados** antes da consolidação.

### 4. Tecnologias Utilizadas

* Spark
* Python
* Pandas
* Matplotlib
* Seaborn
* GeoPandas
* AWS
* AWS Glue
* Jupyter Notebook

### 5. Estrutura do Projeto

```text
│
├── data/
├── notebooks/
│   ├── 01_bronze_ingestao.ipynb
│   ├── 02_silver_consolidacao.ipynb
│   ├── 03_gold_selecao.ipynb
│   └── Construção dos gráficos.ipynb
│
├── scripts/
│   └── 02_silver_glue_jobs.py
│
└── README.md
```

### 6. Metodologia

O desenvolvimento do projeto foi dividido nas seguintes etapas:

1. Ingestão dos dados;
2. Construção da camada Bronze;
3. Mapeamento e harmonização das colunas;
4. Consolidação dos arquivos na camada Silver;
5. Seleção das variáveis relevantes;
6. Tratamento das colunas booleanas;
7. Construção da camada Gold;
8. Geração dos gráficos;
9. Análise dos resultados;
10. Geração de insights e recomendações.

### 7. Arquitetura

O projeto utiliza uma arquitetura baseada nas camadas **Bronze, Silver e Gold**, executada em ambiente AWS.

```text
Dados brutos
     ↓
  Bronze
     ↓
  Silver
     ↓
   Gold
     ↓
Análises e Gráficos
```

* **Bronze:** preparação inicial dos dados;
* **Silver:** mapeamento, tratamento e consolidação das diferentes edições;
* **Gold:** seleção das variáveis utilizadas nas análises.

### 8. Análises Realizadas

Foram realizadas análises para responder às principais questões propostas pelo desafio:

* Como está estruturado o mercado brasileiro de Dados?
* Quais perfis profissionais são mais valorizados?
* Qual é o cenário de diversidade de gênero?
* Quais tecnologias apresentam maior adoção?
* Qual é o índice de adoção de Inteligência Artificial e seu impacto?
* Existem diferenças por região, senioridade e modelo de trabalho?
* Quais são as oportunidades e desafios para empresas que investem em Dados e IA?

### 9. Principais Resultados

A análise identificou alguns dos principais aspectos do mercado brasileiro de Dados:

* Predominância de profissionais **Pleno e Sênior**;
* Forte concentração de profissionais na região **Sudeste**, especialmente em São Paulo;
* **SQL e Python** como principais linguagens utilizadas;
* **Power BI** como destaque entre as ferramentas de BI;
* **AWS** como principal tecnologia de Cloud;
* Predominância dos modelos de trabalho **remoto e híbrido**;
* Disparidade de gênero no mercado de Dados;
* Crescente adoção de **Inteligência Artificial Generativa**;
* Maior remuneração associada à senioridade, experiência e especialização.

### 10. Conclusão

O projeto permitiu integrar conceitos de **Engenharia de Dados e Analytics** para transformar diferentes edições da pesquisa State of Data Brasil em uma base analítica consolidada.

A utilização das camadas **Bronze, Silver e Gold** possibilitou organizar, tratar e harmonizar os dados antes da realização das análises.

Os resultados demonstram um mercado de Dados em consolidação, com forte presença de SQL, Python, Power BI e Cloud, além de uma crescente utilização de Inteligência Artificial.

As análises também evidenciam desafios relacionados à **diversidade de gênero, concentração geográfica de talentos e escassez de profissionais altamente especializados**.

### Autores

* Fabio Silveira Beneti
* Jéssica Vieira de Souza
* João Pedro Brito Oliveira
* Mateus Cabral Gama Oliveira
* Matheus Barros de Santana

**Projeto desenvolvido para o Tech Challenge – Fase 3 – Pós Tech Data Analytics – FIAP**

