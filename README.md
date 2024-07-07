# Escopo do projeto
Este projeto equivale à 3ª avaliação da disciplina "Coleta, preparação e análise de dados" dos cursos de graduação em (i) Ciência de dados e (ii) Engenharia de software.

O código desenvolvido tem duas finalidades principais:
1. Extrair dados do Sistema de Internações Hospitalares do SUS e transformá-los.
2. Criar _dashboards_ de Power BI, buscando visualizar os dados de maneira simples e interativa.



## Como rodar o projeto
1. clone o projeto para o seu repositório;
2. crie um ambiente virtual no diretório raiz da aplicação:

        python -m venv .venv

3. ative o ambiente virtual recém criado:

        source ./.venv/bin/activate

4. instale as dependências necessárias

        pip install -r ./requirements.txt

## Como extrair os dados a partir do SIH-SUS
Para realizar a extração de dados a partir do SIH, abra um terminal, vá até a raiz do projeto e digite:
                
        python main.py extract uf ano_inicial ano_final

Por exemplo, para extrair dados do RS para os anos de 2015 e 2016, rode o seguinte comando:

        python main.py extract RS 2015 2016

## Estrutura do projeto
1. Os arquivos de dados estão na pasta `./data`;
2. Os `scripts` de extração estão no diretório `extract`;
3. Os `scripts` de transformação estão no diretório `transform`;

## Fonte de dados
Para realizar a extração de dados do SIH, foi utilizada a biblioteca _pysus_ escrita em Python. Foram baixados os dados dos anos de 2015 e 2016, para o Estado do Rio Grande do Sul, na modalidade RD-Reduzida. 

Foram também utilizadas como fontes de dados: 

 - Tabela contendo as subcategorias CID-10: dados obtidos a partir de 
        https://github.com/cleytonferrari/CidDataSus/tree/master/CIDImport/Repositorio/Resources 

 

 - Tabela contendo a relação de estados com seus nomes e siglas: dados obtidos a partir de 
        https://github.com/leogermani/estados-e-municipios-ibge/blob/master/estados.csv  

 - Tabela contendo a latitude e longitude dos municípios brasileiros: dados obtidos a partir de
        https://github.com/kelvins/municipios-brasileiros/blob/main/csv/municipios.csv


## Link úteis
https://pcdas.icict.fiocruz.br/conjunto-de-dados/sistema-de-informacoes-hospitalares-do-sus-sihsus/dicionario-de-variaveis/
https://repositorio.ipea.gov.br/bitstream/11058/9409/1/Uma_analise_da_base_de_dados_do_sistema_de_informacao_hospitalar.pdf


<div>
 <iframe title="t3_dashboards" width="1024" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiOTJkYzEwNWQtOGZhZC00OGI3LTlkYmQtZTE0YTk1NTMzYTVmIiwidCI6ImQwOTBlODc5LWJkOTItNDJlNS1iOGJhLTk3ZjMxZjY1ZmM1YyJ9" frameborder="0" allowFullScreen="true"></iframe>
</div>
