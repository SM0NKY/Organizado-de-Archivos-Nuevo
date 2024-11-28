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
        
        self.ventana_abierta:bool = False

        self.geometry("350x600")
        self.title("Tipos de Archivo")
        self.label1:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text="Selecciona los formatos que quieras organizar", font= ("Comic Sans MS", 15))
        self.tipos:Optional[List[Any]] = [elemento for elemento in self.clasific.clasificar_tipos() if elemento.strip()] if self.lista_clasificado else clasificaciones
        self.check_boxes:Optional[List[object]]|Optional[List[customtkinter.CTkCheckBox]] = []
        self.values:Optional[Dict[str,object]]|Optional[Dict[str,customtkinter.BooleanVar]] = {}
        
        self.label1.pack(padx = 20, pady= 20)
        self.load_combo_boxes()

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
        self.update_combo_boxes()
        self.button_c.pack() 
        self.deiconify()
        self.ventana_abierta = True

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
        >>> objeto: object|Tipos = Tipos()
        >>> objecto.close()
        {None} -> Withdraws the window from the screen and saves the config files
        """
        
        try:
            with open(os.path.join(Path(__file__).parent,"filetypes.json"),'w') as file:
                json.dump({"types":self.listado_de_seleccion()},file)

            self.ventana_abierta = False
            self.withdraw()
        
        except Exception as error:
            ic(error)
            raise error

    def listado_de_seleccion(self) -> Optional[List[str]]:
        """ This method verifies which is the selected data within the filetypes
        Parameters
        ----------
        `None`

        Return
        ----------
        `Optional[List[str]]` 

        Example
        ----------
        >>> objeto:object|Tipos = Tipos()
        >>> objeto.listado_de_seleccion()
        {Optional[List[str]]}
        """
        try:
            return [tipo for tipo in self.values.keys() if self.values[tipo].get()]
        except Exception as error:
            ic(error)
            raise error
        
    def load_combo_boxes(self) -> None:
        """This method loads the correspondent filetypes in the window
        
        Parameters
        ----------
        `None`

        Return 
        ----------
        `None`

        Example
        ----------
        >>> objeto:object|Tipos = Tipos()
        >>> objeto.load_combo_boxes()
        {None} -> Loads the combo boxes in the window

        """

        for box in self.check_boxes:
            box.destroy()

        self.check_boxes:Optional[List[object]]|Optional[List[customtkinter.CTkCheckBox]] = []
        self.values.clear()

        for tipo,index in zip(self.tipos,range(len(self.tipos))):
                self.values[tipo] = customtkinter.BooleanVar()
                self.check_boxes.append(customtkinter.CTkCheckBox(self, text= tipo, variable= self.values[tipo]))
                self.check_boxes[index].pack(padx = 10, pady = 2,side = "top", anchor = "w")
            

    def update_combo_boxes(self) -> None:
        nuevos_tipos = Clasify_F().clasificar_tipos()
        if nuevos_tipos != self.tipos:
            
            self.tipos = [elemento for elemento in nuevos_tipos if elemento.strip()]
            self.load_combo_boxes()

if __name__ == "__main__":
    tipos:object|Tipos = Tipos()
    tipos.mostrar()
