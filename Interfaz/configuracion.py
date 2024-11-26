import customtkinter
from icecream import ic
from typing import List, Dict, Any, Optional
from pathlib import Path
import os
import json


class Configuracion(customtkinter.CTk):
    def __init__(self) -> object:
        super().__init__()
        self.geometry("300x200")
        self.title("Configuración")
        self.withdraw()
        self.label1:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text="Seleccione el directorio de entrada")
        
        with open(os.path.join(Path(__file__).parent.parent,"Archivos_e","directorio_e.json"),'r') as input:
            dir_entrada:dict|json.load = json.load(input)
            self.label2:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text= dir_entrada.get("directory"), font= ("Comic Sans MS",20)) 

        self.label3:object|customtkinter.CTK

        with open(os.path.join(Path(__file__).parent.parent,"Archivos_carpetas","directorio_s.json"))as output:
            dir_salida:dict|json.load = json.load(output)
            self.label4:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text=dir_salida.get("o_directory"), font= ("Comic Sans MS", 20))

    def mostrar(self) -> None:
        self.deiconify()

    def ocultar(self) -> None:
        self.withdraw()

    
    def configurar_e(self) -> Optional[str]:
        try:
            directorio:str  = customtkinter.filedialog.askdirectory()
            with open(os.path.join(Path(__file__).parent.parent,"Archivos_e","directorio_e.json"),'r') as file:
                json.dump({"directory":os.path.normpath(directorio)},file)

        except FileNotFoundError as error:
            ic(error)
            raise error
        
    def configurar_s(self) -> Optional[str]:
        try:
            directorio:str = customtkinter.filedialog.askdirectory()
            
            with open(os.path.join(Path(__file__).parent.parent,"Archivos_carpetas","directorio_s.json")) as file:
                json.dump({"o_directory":os.path.normpath(directorio)})
        except FileNotFoundError:
            ic(FileNotFoundError)
            raise FileNotFoundError
    
    
        
    
    
            
