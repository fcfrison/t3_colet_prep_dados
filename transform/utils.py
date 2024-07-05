import pandas as pd
from typing import List
from utils.utils import get_subdirectories
from config import *

def load_files()->pd.DataFrame:
    list_of_files : List[pd.DataFrame] = []
    list_of_dirs = get_subdirectories(SIH_DIR)
    for item in list_of_dirs:
        list_of_files.append(pd.read_parquet(item))
    return pd.concat(list_of_files)
# Cria tabela time_table - agrupando por ano e mês
def create_time_table(df:pd.DataFrame)->pd.DataFrame:
    selected_columns : List[str] = ['ANO_CMPT','MES_CMPT']
    df_time_table :pd.DataFrame = df[selected_columns]
    df_time_table = df_time_table.drop_duplicates(subset=selected_columns)
    return df_time_table.sort_values(by=selected_columns)
def create_time_table_key(df:pd.DataFrame)->pd.DataFrame:
    df['TIME_KEY'] = df['ANO_CMPT'] + '|' + df['MES_CMPT']
    return df
def create_paciente_table(df:pd.DataFrame)->pd.DataFrame:
    df_paciente_table = df[['N_AIH','NASC','SEXO']]
    df_paciente_table = df_paciente_table.drop_duplicates()
    df_paciente_table = df_paciente_table.rename(columns={'N_AIH':'ID_PACIENTE'})
    df_paciente_table.drop_duplicates(subset='ID_PACIENTE',inplace=True)
    return df_paciente_table
def convert_date_to_datetime(df:pd.DataFrame)->pd.DataFrame:
    df['NASC'] = pd.to_datetime(df['NASC'], format='%Y%m%d')
    df['NASC'] = df['NASC'].dt.strftime('%d/%m/%Y')
    return df
def create_municipios_table()->pd.DataFrame:
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
# Define key da cid-10
def create_cid_10_key(df:pd.DataFrame)->pd.DataFrame:
    df_cid_10 = df.rename(columns={'DIAG_PRINC':'CID_10_KEY'})
    df_cid_10['CID_10_KEY'] = df_cid_10['CID_10_KEY'].transform(func=lambda arg:arg[:3])
    return df_cid_10
# importa tabela de categorias da CID-10
def create_cid_table()->pd.DataFrame:
    df_cid : pd.DataFrame= pd.read_csv(filepath_or_buffer=CID_DATA/'cid_10.csv',sep=';',encoding='iso-8859-1')
    select_columns : List[str] = ['CAT','DESCRICAO']
    df_cid = df_cid[select_columns]
    df_cid.rename(columns={'CAT':'CID_10_KEY'})
    return df_cid
def clean_numeric_columns(df:pd.DataFrame)->pd.DataFrame:
    df_sih = df
    df_sih['QT_DIARIAS'] = df_sih['QT_DIARIAS'].str.strip()
    df_sih['VALOR_INTERNACAO'] = df_sih['VALOR_INTERNACAO'].str.strip()
    dtypes : dict = {
                        'QT_DIARIAS':int,
                        'VALOR_INTERNACAO':float
                    } 
    df_sih = df_sih.astype(dtype=dtypes)
    return df_sih