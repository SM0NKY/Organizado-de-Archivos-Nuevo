import customtkinter
from icecream import ic
import time

class Contador_de_Archivos(customtkinter.CTk):
    """ This object displays the current progress of the movement of the files
    Atributes
    ----------
    `None`

    Example
    ----------
    >>>objeto:object|Contador_de_Archivos = Contador_de_Archivos()
    {objeto}
    """

    def __init__(self):
        super().__init__()
        self.title = "Contador"
        self.geometry("300x200")
        self.protocol("WM_DELETE_WINDOW",lambda: None)
        self.label_counter:object|customtkinter.CTkLabel = customtkinter.CTkLabel(master= self,text = "", font= ("Comic Sans MS",20))
        self.barra_de_progreso:object|customtkinter.CTkProgressBar = customtkinter.CTkProgressBar(self, width= 400, progress_color= "Green")

    def show(self) -> None:
        """This function shows the progress bar in the screen
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `None`
        """
        
        self.label_counter.pack(padx = 20, pady = 20)
        self.barra_de_progreso.pack(padx = 20, pady = 20)

    def ocultar(self) -> None:
        self.withdraw()

    def progress_bar(self,number:int,total:int) -> None:
        """This function changes the progress in the progress bar, it automatically displays the progressbar and closes for it self
        Parameters
        ----------
        :number: `int` -> The current position in the loop
        :total: `int` -> The total items to be used

        Return
        ----------
        `None`
        """ 
        try:    
            self.barra_de_progreso.update_idletasks()
            self.barra_de_progreso.set(number/total)
            self.label_counter.configure(text = f"Archivo {number} de {total}")
            time.sleep(0.5)
        except Exception as e:
            ic(e)
            raise e

if __name__ == "__main__":
    objeto:Contador_de_Archivos = Contador_de_Archivos()
    for x in range(10):
        objeto.progress_bar(x+1,10)