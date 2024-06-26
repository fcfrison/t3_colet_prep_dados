import pandas as pd
from main import load_files


def transform()->None:
    # desenvolver aqui a rotina principal de transformação
    df_sih: pd.DataFrame = load_files()

