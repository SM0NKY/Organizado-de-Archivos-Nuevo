import customtkinter,sys
from typing import Any, List, Dict, Optional
from icecream import ic
import json
from pathlib import Path
import os

sys.path.append(os.path.normpath(Path(__file__).parent.parent))
from Archivos_e import Clasify_F


class Tipos(customtkinter.CTk):
    """ This class allows to show a screen 
    Atributes
    ----------
    :clasificaciones: `Optional[List[str]]` -> It uses default paths in case

    Example
    >>> objeto:object|Tipos = Tipos()
    {None} -> Object
    """
    try:
        clasific:object|Clasify_F = Clasify_F()
        lista_clasificado:Optional[List[str]] = clasific.clasificar_tipos()
    except Exception as error:
        ic(error)
        

    def __init__(self,clasificaciones:Optional[List[str]] = None) -> None:
        super().__init__()
        
        self.geometry("300x600")
        self.title("Tipos de Archivo")
        self.label1:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text="Selecciona los formatos que quieras organizar", font= ("Comic Sans MS", 10))
        self.tipos:Optional[List[Any]] = self.lista_clasificado  if self.lista_clasificado else clasificaciones
        self.check_boxes:Optional[List[object]]|Optional[List[customtkinter.CTkCheckBox]] = []
        self.values:Optional[Dict[str,object]]|Optional[Dict[str,customtkinter.BooleanVar]] = {}

        for tipo in self.tipos:
            self.values[tipo] = customtkinter.BooleanVar()
        
        for tipo in self.tipos:
            self.check_boxes.append(customtkinter.CTkCheckBox(self, text= tipo, variable= self.values[tipo]))

        self.button_c:object|customtkinter.CTkButton = customtkinter.CTkButton(self, text= "Confirmar", font=("Comic Sans",15),command=self.close )

    def mostrar(self) -> None:
        """ It shows the window on the screen, within the mainloop of a main window

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> objeto: object|Tipos = Tipos()
        >>> objeto.mostrar()
        {None} -> Displays the window on the screen
        """

        self.label1.pack(padx = 20, pady= 20)
        self.load_combo_boxes()
        self.button_c.pack()

        #self.mainloop()
        self.deiconify()

    def close(self):
        """ It withdraws the window from the screen 
        Prameters
        ----------
        `None`

        Return 
        ----------
        `None`

        Example
        ----------
        >>>
        """
        
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
        
    def load_combo_boxes(self) -> None:
        for index in range(len(self.check_boxes)):
            self.check_boxes[index].pack(padx = 10, pady = 2,side = "top", anchor = "w")

if __name__ == "__main__":
    tipos:object|Tipos = Tipos()
    tipos.mostrar()
