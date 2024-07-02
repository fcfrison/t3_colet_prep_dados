from typing import List
from pysus.ftp.databases.sih import SIH
from pysus.ftp import File, Database
from utils.utils import create_folder
from config.dir_config import SIH_DIR
def extract()->None:
    create_folder(path=SIH_DIR)
    sih : Database = SIH().load()
    sih_list_files : List[File] = sih.get_files("RD", uf="RS", year=2015)
    sih.download(files=sih_list_files, local_dir=SIH_DIR)