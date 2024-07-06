import sys
from extract import extract
from transform import transform_data
if sys.argv[1]=='extract':
    uf : str = sys.argv[2]
    ano_inicial : int = int(sys.argv[3])
    ano_final : int = int(sys.argv[4])
    extract(ano_inicial=ano_inicial,ano_final=ano_final,uf=uf)
if sys.argv[1]=='transform':
    transform_data()