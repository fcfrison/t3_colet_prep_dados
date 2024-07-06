import os
from typing import List
def create_folder(path:str)->None:
    """
    Cria uma pasta no diretório especificado.

    Esta função cria uma pasta no caminho fornecido, caso ela ainda não exista.

    Argumento:
        path (str): Caminho completo para a pasta a ser criada.

    Retorno:
        None
    """
    if not os.path.exists(path): 
        os.makedirs(path)
def get_subdirectories(parent_directory:str)->List[str]:
    """
    Obtém uma lista de subdiretórios dentro de um diretório pai.

    Esta função retorna uma lista contendo os caminhos completos de todos os subdiretórios
    presentes no diretório fornecido.

    Argumento:
        parent_directory (str): Caminho completo para o diretório pai.

    Retorno:
        List[str]: Lista contendo os caminhos completos dos subdiretórios.
    """
    subdirectories : List[str] = []
    for item in os.listdir(parent_directory):
        item_path : str  = os.path.join(parent_directory, item)
        subdirectories.append(item_path)
    return subdirectories