import customtkinter
from customtkinter import CTkButton as Button
from typing import Dict, Any, List, Optional
import sys
from tkinter import messagebox
from icecream import ic
from configuracion import Configuracion
from seleccion import Tipos
import json
import os
from pathlib import Path
import time

sys.path.append(os.path.abspath(os.path.join(Path(__file__).parent.parent,"Archivos_carpetas")))
from Archivos_carpetas import Create_Folders

sys.path.append(os.path.abspath(os.path.join(Path(__file__).parent.parent,"Mover_Archivos")))
from Mover_Archivos import Organizar

class Ventana(customtkinter.CTk):
    """This class displays the principal window of the program
    
    Atributes
    ----------
    `None`

    Example
    ----------
    >>> window:object|Ventana = Ventana()
    >>> window
    {Object} 
    """
    
    configuracion:object|Configuracion = Configuracion()
    seleccion:object|Tipos =  Tipos()
    
    opciones:List = ["Ordenar Archivos", "Crear carpetas","Todas las Anteriores"]

    var:str|object|customtkinter.StringVar = customtkinter.StringVar(value=opciones[0])
    def __init__(self):
        super().__init__()
        self.ventana_secundaria:bool = False
        self.geometry("500x600")
        self.title("Interfaz")
        self.protocol("WM_DELETE_WINDOW",self.close)
        self.frame = customtkinter.CTkFrame(self, width= 150, corner_radius= 10, fg_color="#fac8af")
        
        self.config_button:object|customtkinter.CTkButton = customtkinter.CTkButton(self.frame,text= "Configuración",command= self.open_config,font= ("Sans Seriff",15),fg_color="#e89323")
        self.selec_button:object|customtkinter.CTkButton = customtkinter.CTkButton(self.frame,text="Tipos de Archivo", command= self.open_types, font=("Sans Seriff", 15), fg_color= "#e89323")
        self.label1:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self, text="Que acción quieres realizar", font= ("Sans Seriff", 15))
        
        self.option_menu:object|customtkinter.CTkOptionMenu = customtkinter.CTkOptionMenu(self, variable= self.var, values= self.opciones, fg_color="#21586F", button_color="#21586F")

        self.conirm_action:object|customtkinter.CTkButton  = customtkinter.CTkButton(self, text= "Confirmar", font= ("Sans Seriff", 15), command= self.confirm_command)

    def main(self) -> None:
        """This function starts the mainloop, and initializes the correspondent labels, buttons, etc.
        
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `None`

        Example
        ----------
        >>> window
        >>> window:object|Ventana = Ventana()
        >>> window.main()
        {None} -> Displays the main window in the screen 
        """
        #Aqui adjuntar lo que se ocupa mostrar en pantalla#
        self.initialize_structure()
        self.mainloop()

    def close(self) -> None:
        """This function closes the main window and all the code
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `None`

        Example
        >>> ventana:object|Ventana()
        >>> ventana.open() -> Opens the window
        >>> ventana.close() -> Closes the window
        {None} -> Closes the window
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
        
        Return
        ----------
        `None`

        Example
        ----------
        >>> window:object|Ventana = Ventana()
        >>> window.initialize_structure()
        {None} -> It initializes the window structure
        """
        self.frame.pack(side = "left", fill = "y", padx = 10, pady = 10)
        self.config_button.pack(padx = 10, pady = 15)
        self.selec_button.pack(padx = 10, pady = 15)
        self.label1.pack(padx = 10, pady = 20)
        self.option_menu.pack(pady = 20)
        self.conirm_action.pack()
        
    
    def open_config(self) -> None:
        """ This method opens the configuration window to adjust the input location file and the output location file

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> window:object|Ventana = Ventana()
        >>> window.open_config()
        {None} -> Opens the window configuration window
        """ 
        try:
            if not (self.configuracion.ventana_abierta or self.seleccion.ventana_abierta):
                self.configuracion.mostrar()
        except Exception as error:
            ic(error)

    def open_types(self) -> None:
        """ This method opens a types list to select the desired filetypes

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> window:object|Ventana = Ventana()
        >>> window.open_types()
        {None} -> Opens the filetypes window
        """
        try:

            if not (self.configuracion.ventana_abierta or self.seleccion.ventana_abierta):
                self.seleccion.mostrar()
        except Exception as error:
            ic(error)


    def confirm_command(self):
        """This method confirms the current selected option and makes actions accordantly of the option
        
        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        -----------
        >>> window:object|Ventana = Ventana()
        >>> window.confirm_command()
        {None} -> Takes the correspondent selected actions
        """
        try: 
            if self.option_menu.get() == self.opciones[0]:
                print("Moviendo Archivos")
                self.move_files()
            elif self.option_menu.get() == self.opciones[1]:
                print("Creando Carpetas")
                if not self.seleccion.listado_de_seleccion() == []:
                    print(self.seleccion.listado_de_seleccion())
                    self.create_folders()
            elif self.option_menu.get() == self.opciones[2]:
                print("Creando y Ordenando Archivos")
                self.create_folders()
                self.move_files()
        except Exception as e:
            ic(e)
            messagebox.askokcancel("Error","Por favor resvisa la informacion ingresada")  
    
    def get_types(self) -> Optional[List[str]]:
        """ This function obtains the selected types from the json file

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        >>> window:object|Ventana = Ventana()
        >>> window.get_types()
        {Optional[List]} -> Returns the selected filetypes
        """
        try:
            with open(os.path.join(Path(__file__).parent,"filetypes.json")) as filetypes:
                open_filetypes:json.load|dict = json.load(filetypes)
                return open_filetypes.get("types")
        except Exception as error:
            ic(error)

    def create_folders(self) -> None:
        """ This method creates the correspondent files to organize them

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        >>> window:object|Ventana = Ventana()
        >>> window.create_folders()
        {None} -> Creates the correspondent folders
        """
        create:object|Create_Folders = Create_Folders()
        create.folders(self.seleccion.listado_de_seleccion())

    def move_files(self) -> None:
        """This method moves the files to its correspondent destination

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> window:object|Ventana = Ventana()
        >>> window.move_files()
        {None} ->  Moves the files to their correspondent locations

        """
        try:
            if self.seleccion.listado_de_seleccion():
                organize:object|Organizar = Organizar()
                tiempo:int  = 1000*len(self.seleccion.listado_de_seleccion())
                self.after(tiempo, lambda: organize.move_files(self.seleccion.listado_de_seleccion()))
        except Exception as error:
            ic(error)


if __name__ == "__main__":
    window:object|Ventana = Ventana()
    window.main()
        
        