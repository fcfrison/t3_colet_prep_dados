import os
from pathlib import Path
from utils.utils import create_folder
ROOT_DIR : str = Path(os.getcwd())
DATA_DIR : str = ROOT_DIR/"data"
SIH_DIR : str = DATA_DIR/"sih"
IBGE_DATA : str = DATA_DIR/"tabelas_ibge"
CID_DATA : str = DATA_DIR/"cid_10"
OUTPUT : str = DATA_DIR/"output"
create_folder(SIH_DIR)
create_folder(OUTPUT)

