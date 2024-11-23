import os 
import json
from typing import Optional,Dict,Any,List


class Archivos():
    def __init__(self) -> object:
        #-- Aqui debo agregar el directorio --#
        self.directorio:str = Optional[Dict[str]]
        
        with open('','r') as directorio_e:
            self.directorio = json.load(directorio_e)
    

    def documents(self) -> Optional[Dict[str,str]]|None:
        documentos:Dict[str,str] = {}
        try:
            for archivo in os.listdir(self.directorio):
                documentos[self.directorio] = [archivo]
            return documentos
        except Exception as e:
            print("Hubo un error en la clase de los archivos")
            raise ValueError(e)
    
