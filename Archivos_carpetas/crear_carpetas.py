import os
from typing import List, Any, Dict, Optional
from Archivos_e import Clasify_F
from icecream import ic as ice
from pathlib import Path
import json

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

    
    carpetas:List[str] = Clasify_F.clasificar_tipos()
    subcarpetas:List[str] = Clasify_F.clasificar_fecha()
    
    def __init__(self):
        self.output:str = None

        with open(os.path.join(Path(__file__).parent,"directorio_s.json"),'r') as directorio_s:
            if directorio_s:
                dir:dict = json.load(directorio_s)
                self.output:str = dir.get("o_directory")

    def folders(self)-> None:
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
                if not os.path.exists(os.path.join(self.output, carpeta)):
                    os.mkdir(os.path.join(self.output, carpeta))
                    for subcarpeta in self.subcarpetas:
                        if not os.path.exists(os.path.join(self.output,carpeta,subcarpeta)):
                            os.mkdir(os.path.join(self.output,carpeta,subcarpeta))
        except Exception as e:
            ice(e)
            if self.carpetas and self.subcarpetas:
                raise e
        

