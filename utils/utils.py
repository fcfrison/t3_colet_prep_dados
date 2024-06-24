import os
from typing import List
def create_folder(path:str)->None:
    if not os.path.exists(path): 
        os.makedirs(path)
def get_subdirectories(parent_directory:str)->List[str]:
    subdirectories = []
    for item in os.listdir(parent_directory):
        item_path = os.path.join(parent_directory, item)
        subdirectories.append(item_path)
    return subdirectories