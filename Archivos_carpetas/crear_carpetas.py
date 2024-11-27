import os,sys
from typing import List, Any, Dict, Optional
from icecream import ic as ice
from pathlib import Path
import json

sys.path.append(os.path.normpath(Path(__file__).parent.parent))
from Archivos_e import Clasify_F

class Create_Folders():
    """ This class creates the correspondent folders needed for the files
    Atributes
    ---------                
    `None`
    
    Example
    ---------
    >>> objeto:object|Create_Folders()
    {objeto} 
    """

    names:object|Clasify_F = Clasify_F()
    carpetas:List[str] = names.clasificar_tipos()
    subcarpetas:List[str] = names.clasificar_fecha()
    
    def __init__(self):
        self.output:str = None

        with open(os.path.join(Path(__file__).parent,"directorio_s.json"),'r') as directorio_s:
            if directorio_s:
                dir:dict = json.load(directorio_s)
                self.output:str = dir.get("o_directory")

    def folders(self,Seleccion:Optional[List[str]] = None)-> None:
        """This method creates the correspondent folders and subfolders
        Parameters
        ----------
        `None`

        Return
        ---------
        `None`
        """

        try:
            for carpeta in self.carpetas:
                ice(carpeta)
                if carpeta in Seleccion: 
                    if not os.path.exists(os.path.join(self.output, carpeta)):
                        ice(os.path.exists(os.path.join(self.output, carpeta)))
                        os.makedirs(os.path.join(self.output, carpeta))
                        ice(self.subcarpetas)
                        for subcarpeta in self.subcarpetas:
                            if not os.path.exists(os.path.join(self.output,carpeta,subcarpeta)):
                                ice(os.path.join(self.output,carpeta,subcarpeta))
                                os.makedirs(os.path.join(self.output,carpeta,subcarpeta))
        except Exception as e:
            ice(e)
            if self.carpetas and self.subcarpetas:
                raise e
        

