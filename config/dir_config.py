import os
from pathlib import Path
ROOT_DIR : str = Path(os.getcwd())
DATA_DIR : str = ROOT_DIR/"data"
SIH_DIR : str = DATA_DIR/"sih"
IBGE_DATA : str = DATA_DIR/"tabelas_ibge"