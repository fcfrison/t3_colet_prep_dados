from typing import List
import pandas as pd
from utils.utils import get_subdirectories
from config import DATA_DIR

def load_files()->pd.DataFrame:
    list_of_files : List[pd.DataFrame] = []
    list_of_dirs = get_subdirectories(DATA_DIR)
    for item in list_of_dirs:
        list_of_files.append(pd.read_parquet(item))
    return pd.concat(list_of_files)