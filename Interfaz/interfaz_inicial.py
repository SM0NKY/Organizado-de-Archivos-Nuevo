
import customtkinter
from customtkinter import CTkButton as Button
from typing import Dict, Any, List, Optional
import sys
from tkinter import messagebox
from icecream import ic


class Ventana(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x800")
        self.title = "Interfaz"
        self.protocol("WM_DELETE_WINDOW")

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
        """ This function initializes the buttons and labels
        """

        
        