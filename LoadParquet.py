import threading
from typing import List
import pandas as pd 
class LoadParquet(threading.Thread): 
    def __init__(self, path_file:str,
                list_of_files:List[pd.DataFrame],
                sema_mutex_list_of_files:threading.Semaphore): 
        threading.Thread.__init__(self)  
        self.path_file = path_file
        self.list_of_files = list_of_files
        self.sema = sema_mutex_list_of_files

    def run(self): 
        df:pd.DataFrame = pd.read_parquet(path=self.path_file)
        # utilizando um mutex p/evitar racing conditions
        self.sema.acquire()
        self.list_of_files.append(df)
        self.sema.release()
