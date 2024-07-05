import sys
from extract import extract
from transform import transform_data
if sys.argv[1]=='extract':
    ano_inicial : int = int(sys.argv[2])
    ano_final : int = int(sys.argv[3])
    #extract(ano_inicial=ano_inicial,ano_final=ano_final)
if sys.argv[1]=='transform':
    transform_data()