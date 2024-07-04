from typing import List
from pysus.ftp.databases.sih import SIH
from pysus.ftp import File, Database
from utils.utils import create_folder
from config.dir_config import SIH_DIR
def extract(ano_inicial:int, ano_final:int)->None:
    create_folder(path=SIH_DIR)
    sih : Database = SIH().load()
    for ano in range(ano_inicial,ano_final+1):
        sih_list_files : List[File] = sih.get_files("RD", uf="RS", year=ano)
        sih.download(files=sih_list_files, local_dir=SIH_DIR)