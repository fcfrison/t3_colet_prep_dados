import time
from typing import List
from threading import Semaphore
import pandas as pd
from utils.utils import get_subdirectories
from config import DATA_DIR
from LoadParquet import LoadParquet
def load_files()->pd.DataFrame:
    # Instancia sema mutex
    sema_mutex_list_files = Semaphore(1)
    list_of_files : List[pd.DataFrame] = []
    list_of_dirs = get_subdirectories(DATA_DIR)
    thread_list : List[LoadParquet] = []
    for item in list_of_dirs:
        thread_list.append(LoadParquet(path_file=item,
                                    sema_mutex_list_of_files=sema_mutex_list_files,
                                    list_of_files=list_of_files))
    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
    return pd.concat(list_of_files)

def load_files_sem_threads()->pd.DataFrame:
    list_of_files : List[pd.DataFrame] = []
    list_of_dirs = get_subdirectories(DATA_DIR)
    for item in list_of_dirs:
        list_of_files.append(pd.read_parquet(item))
    return pd.concat(list_of_files)
start_time = time.time()
load_files()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")