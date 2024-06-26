import pandas as pd
from main import load_files


def transform()->None:
    # desenvolver aqui a rotina principal de transformação
    df: pd.DataFrame = load_files()

