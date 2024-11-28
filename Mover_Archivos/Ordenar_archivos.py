import shutil as sh
from typing import List, Dict, Any, Optional
import os
from pathlib import Path
import json,sys
import threading as th

sys.path.append(os.path.abspath(Path(__file__).parent.parent))
from Archivos_e import Clasify_F
from icecream import ic
from Contador_de_Archivos import Contador_de_Archivos

class Organizar(Clasify_F):
    """ This class allows to calculate the final document list and to move the files
    Atributes
    ----------
    `None`

    Example
    >>> objeto:object|Organizar = Organizar()
    {objeto}
    """
    counter = Contador_de_Archivos()
    

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
    
    def final_document_list(self,seleccion:Optional[List[str]]) -> Optional[List[str]]:
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
        final_dir:Optional[List[List[str]]] = []
        try:
            for dir,data in self.archivos.items():
                if data[3] in seleccion:
                    final_dir.append([dir,os.path.join(self.outputdir, data[3], data[1] + f"{data[2]}" , data[0])])
            return final_dir
        except Exception as e:
            ic(e)
            raise e

    def move_files(self,seleccion:Optional[List[str]]) -> None:
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
            if self.outputdir: 
                
                self.counter.show()
                files_moved:int = self.final_document_list(seleccion) 
                ic(self.final_document_list(seleccion))
                for index in range(len(files_moved)):
                    self.counter.progress_bar(index + 1,len(files_moved))
                    ic(os.path.normpath(files_moved[index][0]))
                    #sh.move(files_moved[index][0],files_moved[index][1]) 
                
                self.counter.ocultar()   
        except Exception as e:
            raise e
    

if __name__ == "__main__":
    pass

        #for x in zip(self.archivos.values()[1],self.archivos.values()[2]): 

