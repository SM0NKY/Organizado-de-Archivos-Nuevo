import customtkinter
from icecream import ic
from typing import List, Dict, Any, Optional
from pathlib import Path
import os
import json
from tkinter import PhotoImage

class Configuracion(customtkinter.CTk):
    """ This class shows the configuration settings of the file
    
    Atributes
    ---------
    :directory_ejson: `str` -> The input configuration file on json
    :directory_sjson: `str` -> The output configuration file on json 

    Example
    ---------
    >>> config: object|Configuracion = Configuracion()
    >>> config.mostrar()
    {None} -> Displays the content in the screen

    """
    
    def __init__(self,directory_ejson:str = os.path.join(Path(__file__).parent.parent,"Archivos_e","directorio_e.json"), directory_sjson:str = os.path.join(Path(__file__).parent.parent,"Archivos_carpetas","directorio_s.json")) -> object:
        super().__init__()
        self.geometry("400x700")
        self.title("Configuración")
        self.label1:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text="Seleccione el directorio de entrada")
        self.ventana_abierta:bool = False
        
        with open(directory_ejson,'r') as input:
            dir_entrada:dict|json.load = json.load(input)
            self.label2:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text= dir_entrada.get("directory"), font= ("Comic Sans MS",15)) 

        self.label3:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text="Seleccione el directorio de salida")
        self.button_e:object|customtkinter.CTkButton = customtkinter.CTkButton(self,text= "Seleccionar directorio", font=("Sans Seriff",15), command= self.configurar_e)

        
        with open(directory_sjson,'r')as output:
            dir_salida:dict|json.load = json.load(output)
            self.label4:object|customtkinter.CTkLabel = customtkinter.CTkLabel(self,text=dir_salida.get("o_directory"), font= ("Comic Sans MS", 15))
        
        self.button_s:object|customtkinter.CTkButton = customtkinter.CTkButton(self, text= "Seleccionar directorio", font= ("SansSeriff",15 ),command= self.configurar_s)

        self.boton_c:object|customtkinter.CTkButton = customtkinter.CTkButton(self,text= "Confirmar",font= ("Sans Seriff",15),command= self.ocultar)
    
    def mostrar(self) -> None:
        """ This methods allows to display the window in the screen 

        Parameters 
        ----------
        `None`

        Return
        ---------
        `None`

        Example
        ---------
        >>> objeto:object|Configuracion = Configuracion()
        >>> objeto.mostrar()
        {None} -> It displays the window in the screen  
        """
        #self.iconphoto(True, PhotoImage(file= os.path.join(Path(__file__).parent,"config.png")))
        self.label1.pack(padx = 20, pady = 20)
        self.label2.pack(padx = 20, pady = 20)
        self.label3.pack(padx = 20, pady = 20)
        self.button_e.pack(padx = 20, pady = 20)
        self.label4.pack(padx = 20, pady = 20)
        self.button_s.pack(padx = 20, pady = 20)
        self.boton_c.pack(padx = 20, pady = 20)
        
        self.ventana_abierta = True
        self.deiconify()

    def ocultar(self) -> None:
        """This method withdraws the window from the screen

        Parameters
        ----------
        `None`

        Return 
        ----------
        `None`

        Example
        ---------
        >>> config:object|Configuracion = Configuracion()
        >>> config.mostrar()
        {None} -> Displays the window on the screen
        >>> config.ocultar()
        {None} -> Withdraws the window from the screen
        """
        self.ventana_abierta = False
        self.withdraw()
        
    
    def configurar_e(self) -> Optional[str]:
        """This method helps to change the dir_i.json
        
        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> config:object|Configuracion = Configuracion()
        >>> config.configurar_e()
        {None} -> asks for a new input dir and changes the initial directory
        """
        try:
            directorio:str  = customtkinter.filedialog.askdirectory()
            ic(os.path.normpath(directorio))

            with open(os.path.join(Path(__file__).parent.parent,"Archivos_e","directorio_e.json"),'w') as file:
                json.dump({"directory":os.path.normpath(directorio)},file)
                self.label2.configure(text = directorio)

        except FileNotFoundError as error:
            ic(error)
            raise error
        
    def configurar_s(self) -> Optional[str]:
        """ This method helps to change the dir_o.json

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> config:object|Configuracion = Configuracion()
        >>> config.configurar_s()
        {None} -> asks for a new output dir and changes the initial directory
        

        """
        
        try:
            directorio:str = customtkinter.filedialog.askdirectory() 
            ic(os.path.normpath(directorio))
            
            with open(os.path.join(Path(__file__).parent.parent,"Archivos_carpetas","directorio_s.json"),'w') as file:
                json.dump({"o_directory":os.path.normpath(directorio)},file)
                self.label4.configure(text = directorio)
        except FileNotFoundError as error:
            ic(error)
            raise error

#Esta funcion es para comprobar que funciona la clase
if __name__ == "__main__":
    configuracion:object|Configuracion = Configuracion()
    configuracion.mostrar()
    
        
    
    
            
