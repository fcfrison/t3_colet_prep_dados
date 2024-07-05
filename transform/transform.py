from typing import List
import pandas as pd
from transform.utils import *


def transform()->None:
    colunas_selecionadas : List[str] = [
    'N_AIH',
    'ANO_CMPT',
    'MES_CMPT',
    'DIAG_PRINC',
    'MUNIC_RES',
    'NASC',
    'SEXO',
    'QT_DIARIAS',
    'VAL_TOT'

]
    df_sih : pd.DataFrame = load_files()
    df_sih = df_sih[colunas_selecionadas]
    df_time_table : pd.DataFrame = create_time_table(df=df_sih)
    df_time_table = create_time_table_key(df_time_table)
    df_paciente_table : pd.DataFrame = create_paciente_table(df_sih)
    df_paciente_table = convert_date_to_datetime(df=df_paciente_table)
    df_municipios_table : pd.DataFrame = create_municipios_table()
    df_estados_table : pd.DataFrame = create_estados_table()
    # Cria time_key
    df_sih['TIME_KEY'] = df_sih['ANO_CMPT'] + '|' + df_sih['MES_CMPT']
    df_sih = create_cid_10_key(df=df_sih)
    df_cid_table : pd.DataFrame = create_cid_table()
    df_sih = df_sih.drop(columns=['NASC', 'SEXO', 'ANO_CMPT', 'MES_CMPT'])
    df_sih = df_sih.rename(columns={'MUNIC_RES':'COD_IBGE','VAL_TOT':'VALOR_INTERNACAO'})
    df_sih = clean_numeric_columns(df=df_sih)
    df_sih = df_sih.groupby(by=['N_AIH','CID_10_KEY','COD_IBGE','TIME_KEY'],
               as_index=False).sum()
    df_time_table.to_csv(path_or_buf=OUTPUT/'time_table.csv',sep=';', index=False)
    df_paciente_table.to_csv(path_or_buf=OUTPUT/'paciente_table.csv',sep=';', index=False)
    df_municipios_table.to_csv(path_or_buf=OUTPUT/'municipios_table.csv',sep=';', index=False)
    df_estados_table.to_csv(path_or_buf=OUTPUT/'estados_table.csv',sep=';', index=False)
    df_cid_table.to_csv(path_or_buf=OUTPUT/'cid_table.csv',sep=';', index=False)
    df_sih.to_csv(path_or_buf=OUTPUT/'internacoes.csv',sep=';',index=False,decimal=',')