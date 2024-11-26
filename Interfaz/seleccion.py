import customtkinter
from typing import Any, List, Dict, Optional
from Archivos_e import Clasify_F
from icecream import ic
import json
from pathlib import Path
import os

class Tipos(customtkinter.CTk, Clasify_F):
    def __init__(self,clasificaciones:Optional[List[str]] = Clasify_F.clasificar_tipos()) -> None:
        super().__init__()
        self.tipos:Optional[List[Any]] = clasificaciones

        self.check_boxes:Optional[List[object]]|Optional[List[customtkinter.CTkCheckBox]] = []
        self.values:Optional[Dict[str,object]]|Optional[Dict[str,customtkinter.BooleanVar]] = {}

        for tipo in self.tipos:
            self.values[tipo] = customtkinter.BooleanVar()
        
        for tipo,indice in zip(self.tipos,range(self.tipos)):
            self.check_boxes.append(customtkinter.CTkCheckBox(self, text= tipo, variable= self.values[indice]))

        self.button_c:object|customtkinter.CTkButton = customtkinter.CTkButton(self, text= "Confirmar", font=("Comic Sans",15) )

    def mostrar(self) -> None:

        self.deiconify()

    def close(self):
        try:
            with open(os.path.join(Path(__file__).parent,"filetypes.json"),'w') as file:
                json.dump({"types":self.listado_de_seleccion()},file)

            self.withdraw()
        
        except Exception as error:
            ic(error)
            raise error

    def listado_de_seleccion(self) -> Optional[List[str]]:
        try:
            return [tipo for tipo in self.values.keys() if self.values[tipo].get()]
        except Exception as error:
            ic(error)
            raise error
        
if __name__ == "__main__":
    tipos:object|Tipos = Tipos()
    tipos.mostrar()
