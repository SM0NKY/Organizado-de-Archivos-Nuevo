
import customtkinter
from customtkinter import CTkButton as Button
from typing import Dict, Any, List, Optional
import sys
from tkinter import messagebox
from icecream import ic
from configuracion import Configuracion

class Ventana(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x800")
        self.title = "Interfaz"
        self.protocol("WM_DELETE_WINDOW")
        self.config_button:object|customtkinter.CTkButton = customtkinter.CTkButton(self,)
        self.frame = customtkinter.CTkFrame(self,)

    def main(self) -> None:
        """This function starts the mainloop, and initializes the correspondent labels, buttons, etc.
        Parameters
        ----------
        `None`
        Return
        ----------
        `None` 
        """
        #Aqui adjuntar lo que se ocupa mostrar en pantalla#
        self.mainloop()

    def close(self) -> None:
        """This function closes the main window and all the code
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `None`
        """
        try:
            if messagebox.askyesnocancel("Cerrar","Deseas cerrar el programa"):
                sys.exit()
        except Exception as error:
            ic(error)
            raise error


    def initialize_structure(self) -> None:
        """ This method initializes the buttons and labels
        
        Parameters
        ----------
        `None`
        
        """

        
        