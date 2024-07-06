import pandas as pd
from typing import List
from utils.utils import get_subdirectories
from config import *

def load_files()->pd.DataFrame:
    """
    Carrega e concatena arquivos Parquet de subdiretórios em um DataFrame.

    Retorna:
        pd.DataFrame: DataFrame resultante da concatenação dos arquivos Parquet.
    """
    list_of_files : List[pd.DataFrame] = []
    list_of_dirs = get_subdirectories(SIH_DIR)
    for item in list_of_dirs:
        list_of_files.append(pd.read_parquet(item))
    return pd.concat(list_of_files)
def create_time_table(df:pd.DataFrame)->pd.DataFrame:
    """
    Cria uma tabela de tempo única a partir das colunas 'ANO_CMPT' e 'MES_CMPT'.
    Args:
        df (pd.DataFrame): DataFrame de entrada com as colunas 'ANO_CMPT' e 'MES_CMPT'.
    Retorna:
        pd.DataFrame: DataFrame com valores únicos de 'ANO_CMPT' e 'MES_CMPT', ordenado.
    """
    selected_columns : List[str] = ['ANO_CMPT','MES_CMPT']
    df_time_table :pd.DataFrame = df[selected_columns]
    df_time_table = df_time_table.drop_duplicates(subset=selected_columns)
    return df_time_table.sort_values(by=selected_columns)
def create_time_table_key(df:pd.DataFrame)->pd.DataFrame:
    df['TIME_KEY'] = df['ANO_CMPT'] + '|' + df['MES_CMPT']
    return df
def create_paciente_table(df:pd.DataFrame)->pd.DataFrame:
    """
    Cria uma tabela de pacientes a partir das colunas 'N_AIH', 'NASC' e 'SEXO'.

    Args:
        df (pd.DataFrame): DataFrame de entrada com as colunas 'N_AIH', 'NASC' e 'SEXO'.

    Retorna:
        pd.DataFrame: DataFrame de pacientes com colunas únicas e renomeadas.
    """
    df_paciente_table = df[['N_AIH','NASC','SEXO']]
    df_paciente_table = df_paciente_table.drop_duplicates()
    df_paciente_table = df_paciente_table.rename(columns={'N_AIH':'ID_PACIENTE'})
    df_paciente_table.drop_duplicates(subset='ID_PACIENTE',inplace=True)
    return df_paciente_table
def convert_date_to_datetime(df:pd.DataFrame)->pd.DataFrame:
    """
    Converte a coluna 'NASC' para o formato de data 'dd/mm/yyyy'.

    Args:
        df (pd.DataFrame): DataFrame de entrada com a coluna 'NASC' no formato 'yyyymmdd'.

    Retorna:
        pd.DataFrame: DataFrame com a coluna 'NASC' convertida para o formato 'dd/mm/yyyy'.
    """
    df['NASC'] = pd.to_datetime(df['NASC'], format='%Y%m%d')
    df['NASC'] = df['NASC'].dt.strftime('%d/%m/%Y')
    return df
def create_municipios_table()->pd.DataFrame:
    """
    Cria uma tabela de municípios a partir de um arquivo CSV do IBGE.

    Args:
        None

    Retorna:
        pd.DataFrame: DataFrame com os dados de municípios, incluindo colunas 'COD_IBGE' e 'COD_UF'.
    """
    dtype : dict = {
        'COD':str,
        'COD UF':str
    }
    df_municipios :pd.DataFrame = pd.read_csv(filepath_or_buffer=IBGE_DATA/'municipios.csv', sep=',',
                                              dtype=dtype)
    df_municipios['COD'] = df_municipios['COD'].transform(func=lambda arg:arg[:6])
    return df_municipios.rename(columns={'COD':'COD_IBGE', 'COD UF':'COD_UF'})
def create_estados_table()->pd.DataFrame:
    dtype:dict={'COD':str}
    df_estados:pd.DataFrame = pd.read_csv(filepath_or_buffer=IBGE_DATA/'estados.csv',sep=',',
                                          dtype=dtype)
    return df_estados.rename(columns={'COD':'COD_UF'})

def create_cid_10_key(df:pd.DataFrame)->pd.DataFrame:
    """
    Cria uma tabela de estados a partir de um arquivo CSV do IBGE.

    Args:
        None

    Retorna:
        pd.DataFrame: DataFrame com os dados dos estados, incluindo a coluna 'COD_UF'.
    """
    df_cid_10 = df.rename(columns={'DIAG_PRINC':'CID_10_KEY'})
    df_cid_10['CID_10_KEY'] = df_cid_10['CID_10_KEY'].transform(func=lambda arg:arg[:3])
    return df_cid_10

def create_cid_table()->pd.DataFrame:
    """
    Cria uma tabela CID a partir de um arquivo CSV.

    Args:
        None

    Retorna:
        pd.DataFrame: DataFrame com as colunas 'CID_10_KEY' e 'DESCRICAO'.
    """
    df_cid : pd.DataFrame= pd.read_csv(filepath_or_buffer=CID_DATA/'cid_10.csv',sep=';',encoding='iso-8859-1')
    select_columns : List[str] = ['CAT','DESCRICAO']
    df_cid = df_cid[select_columns]
    df_cid.rename(columns={'CAT':'CID_10_KEY'})
    return df_cid
def clean_numeric_columns(df:pd.DataFrame)->pd.DataFrame:
    """
    Limpa e converte colunas numéricas em um DataFrame.

    Remove espaços em branco das colunas 'QT_DIARIAS' e 'VALOR_INTERNACAO',
    e as converte para tipos de dados numéricos apropriados.

    Args:
        df (pd.DataFrame): DataFrame de entrada com as colunas 'QT_DIARIAS' e 
        'VALOR_INTERNACAO' como strings.

    Retorna:
        pd.DataFrame: DataFrame com as colunas 'QT_DIARIAS' convertida para int e 
        'VALOR_INTERNACAO' convertida para float.
    """
    df_sih = df
    df_sih['QT_DIARIAS'] = df_sih['QT_DIARIAS'].str.strip()
    df_sih['VALOR_INTERNACAO'] = df_sih['VALOR_INTERNACAO'].str.strip()
    dtypes : dict = {
                        'QT_DIARIAS':int,
                        'VALOR_INTERNACAO':float
                    } 
    df_sih = df_sih.astype(dtype=dtypes)
    return df_sih
def insert_lat_long(df:pd.DataFrame)->pd.DataFrame:
    """
    Inserir em um DataFrame latitudes e longitudes de municípios brasileiros.

    Argumentos:
        df (pd.DataFrame): DataFrame a ser enriquecido.

    Retorno:
        DataFrame com 'COD_IBGE', 'lat' e 'long'.
    """
    dtypes : dict = {
        'codigo_ibge':str,
        'latitude':float,
        'longitude':float
    }
    df_lat_long : pd.DataFrame = pd.read_csv(filepath_or_buffer=IBGE_DATA/'municipios_lat_long.csv',
                                             sep=',',dtype=dtypes)
    selected_columns:List[str]=['codigo_ibge','latitude','longitude']
    rename_dict:dict={
        'codigo_ibge':'COD_IBGE',
        'latitude':'lat',
        'longitude':'long'
    }
    df_lat_long = df_lat_long[selected_columns]
    df_lat_long.rename(columns=rename_dict,inplace=	True)
    df_lat_long['COD_IBGE'] = df_lat_long['COD_IBGE'].transform(func=lambda arg:arg[:6])
    df=df.merge(right=df_lat_long, how='left')
    return df