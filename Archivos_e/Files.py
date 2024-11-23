import os 
import json
from typing import Optional,Dict,Any,List
from pathlib import Path

#Path(__file__).parent

class Archivos():
	""" This class opens the correspondent directory to directorio_e.js and shows the correspondent files in the directory
	Atributes
	----------
	`None`
	"""
	def __init__(self) -> object:
		#-- Aqui debo agregar el directorio --#
		self.directorio:Optional[str] = None


		with open(os.path.join(Path(__file__).parent,"directorio_e.json"),'r') as directorio_e:
			if directorio_e:
				dir:dict = json.load(directorio_e)
				self.directorio = dir.get("directory")

	def documents(self) -> Optional[Dict[str,str]]|None:
		""" This function returns the documents of an especific folder
		Parameters
		----------
		`None`
		Return
		----------
		:None:

		Example
		>>> Archivos().documents()
		"""
		documentos:Dict[str,str] = {}
		try:
			for archivo in os.listdir(self.directorio):
				documentos[os.path.join(self.directorio,archivo)] = [archivo]
			return documentos
		except Exception as e:
			if self.directorio:
				print("Hub un error en la clase de los archivos")
				raise ValueError(e)
			else:
				print("No hay un directorio")



