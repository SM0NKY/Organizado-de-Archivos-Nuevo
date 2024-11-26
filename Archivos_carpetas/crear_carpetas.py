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

    def folders(self,Seleccion)-> None:
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
                if carpeta in Seleccion: 
                    if not os.path.exists(os.path.join(self.output, carpeta)):
                        os.mkdir(os.path.join(self.output, carpeta))
                        for subcarpeta in self.subcarpetas:
                            if not os.path.exists(os.path.join(self.output,carpeta,subcarpeta)):
                                os.mkdir(os.path.join(self.output,carpeta,subcarpeta))
        except Exception as e:
            ice(e)
            if self.carpetas and self.subcarpetas:
                raise e
        

