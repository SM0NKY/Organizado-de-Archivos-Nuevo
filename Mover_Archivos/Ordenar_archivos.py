import shutil as sh
from typing import List, Dict, Any, Optional
import os
from pathlib import Path
import json
from Archivos_e import Clasify_F
from icecream import ic
from Contador_de_Archivos import Contador_de_Archivos

class Organizar(Clasify_F,Contador_de_Archivos):
    """ This class allows to calculate the final document list and to move the files
    Atributes
    ----------
    `None`

    Example
    >>> objeto:object|Organizar = Organizar()
    {objeto}
    """
    def __init__(self) -> object:
        super().__init__()
        self.outputdir:str = None
        self.archivos:Dict[str,List[Any]] = self.clasificar_tipo_fecha()
        with open(os.path.join(Path(__file__).parent.parent,"Archivos_carpetas","directorio_s.json"),'r') as output_dir:
            try:
                if output_dir:
                    open_file:dict = json.load(output_dir)
                    self.outputdir:str = open_file.get("o_directory")
            except FileNotFoundError as e:
                raise(e)
    
    def final_document_list(self,seleccion:List[str]) -> Optional[List[str]]:
        """ This function returns the final documents path within the selection
        Parameters
        ----------
        :seleccion: `List[str]`

        Return
        ---------
        `Optional[List[str]]`

        Example
        >>> objeto:Organizar = Organizar()
        >>> print(objeto.final_document_list(seleccion))
        {[archivos in seleccion]} 
        """
        final_dir:List[str] = []
        try:
            for data in self.docs.values():
                final_dir.append(os.path.join(
                    data[3] if data[3] in self.clasificar_tipos() and data[3] in seleccion else None,
                    data[1] + data[2] if data[1] + data[2] in self.clasificar_tipo_fecha() else None,
                    data[0]
                ))
        except Exception as e:
            ic(e)
            raise e

    def move_files(self) -> None:
        """ This function moves the files from the origin "directory_e.json" folder to the "directorio_s.json" and displays the progress using an inheritance of the progressbar
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `None`

        Example
        ----------
        >>> objeto:Organizar = Organizar()
        >>> objeto.move_files()
        {None} -> Files Moved 
        """
        try:
            if output_dir: 
                self.show()
                files_moved:int = len(self.final_document_list()) 
                for input_dir, output_dir, number in zip(self.docs.keys(),self.final_document_list(),range(self.docs.keys())):
                    self.progress_bar(number,files_moved)
                    sh.move(input_dir,output_dir)    
        except Exception as e:
            ic(e)
            raise e
    



        #for x in zip(self.archivos.values()[1],self.archivos.values()[2]): 

