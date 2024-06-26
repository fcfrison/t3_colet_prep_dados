# t3_colet_prep_dados
Trabalho 3 da disciplina de coleta, preparação e análise de dados.
## Escopo do trabalho
- qual o tempo médio de internação hospitalares por doença?
- o tempo médio de internaçao por doença é diferente entre os diferentes municípios?
- o tempo médio de internação por doença tem reduzido ao longo dos anos?
- qual o tempo médio de internação por doença por faixa etária?
- qual o valor médio de gastos hospitalares por doença?

## Link úteis
https://pcdas.icict.fiocruz.br/conjunto-de-dados/sistema-de-informacoes-hospitalares-do-sus-sihsus/dicionario-de-variaveis/
https://repositorio.ipea.gov.br/bitstream/11058/9409/1/Uma_analise_da_base_de_dados_do_sistema_de_informacao_hospitalar.pdf

## Como rodar o projeto
1. clone o projeto para o seu repositório;
2. crie um ambiente virtual no diretório raiz da aplicação:

        python -m venv .venv

3. ative o ambiente virtual recém criado:

        source ./.venv/bin/activate

4. instale as dependências necessárias

        pip install -r ./requirements.txt

## Edição novas funcionalidade
1. Crie a sua _branch_;
2. Fique à vontade para alterar;
3. Não faça commits na _branch_ __main__;

## Estrutura do projeto
1. Os arquivos de dados estão na pasta `./data`;
2. Os `scripts` de extração estão no diretório `extract`;
3. Os `scripts` de transformação estão no diretório `transform`;

## Fonte de dados
Os dados estão sendo extraídos do site do DATA SUS, especificamente do SIH;
