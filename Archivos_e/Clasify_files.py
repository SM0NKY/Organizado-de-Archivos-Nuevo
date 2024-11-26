import os
from .Files import Archivos
from typing import Dict, Any, List, Optional
from pathlib import Path
import datetime as dt
from icecream import ic

class Clasify_F(Archivos):
	""" This class allows to create just the correspondent folder and subfolder names  
	"""
	meses: dict = {
		1: "Enero",
		2: "Febrero",
		3: "Marzo",
		4: "Abril",
		5: "Mayo",
		6: "Junio",
		7: "Julio",
		8: "Agosto",
		9: "Septiembre",
		10: "Octubre",
		11: "Noviembre",
		12: "Diciembre",
	}
	def __init__(self) -> object:
		super().__init__()
		
		self.docs:dict = self.documents()
		self.carpetas:List[List[str]] = [self.clasificar_fecha(),self.clasificar_tipos()]

	def clasificar_tipos(self) -> Optional[List[str]]:
		""" It clasifies the existent suffixes
		Parameters
		----------
		`None`
		
		Return
		---------
		`Optional[List[str]]`

		Example
		>>> objeto: Clasify_F|object = Clasify_F()
		>>> print(objeto.clasificar_tipos())
		{".pdf",".docx",...}
		"""
		tipos_archivo:set = set()
		try:
			for x in self.docs.keys():
				if x not in tipos_archivo:
					tipos_archivo.add(Path(x).suffix)
			return list(tipos_archivo)
		
		except Exception as e:
			if not self.docs:
				print("Hubo un error al clasificar los tipos de archivo")
				raise e
	
	def clasificar_fecha(self) -> Optional[List[str]]:
		""" It clasifies the existent dates
		Parameters
		----------
		`None`

		Return 
		`Optional[list[str]]`

		Example
		---------
		>>> objeto:Clasify_F|object = Clasify_F()
		>>> print(objeto.clasificar_fechas)
		{("Noviembre","2024")...}
		"""
		dates:set = set()
		try:
			for x in self.docs.keys():
				date:dt.datetime = dt.datetime.fromtimestamp(Path(x).stat().st_ctime)
				dates.add(self.meses.get(date.month,None) + date.year )
			return list(dates)
		except Exception as e:
			if not self.docs:
				print("Hubo un error al clasificar las fechas")
				raise e
	
	def clasificar_tipo_fecha(self) -> Optional[Dict[str,List[str]]]:
		"""It makes an dictionary with the necesary specs to clasify a file 
		Parameters
		----------
		`None`
		Return
		
		"""

		nueva_clasificacion:Dict[str,List] = {}
		try:
			for file_path in self.docs.keys():
				file_date:dt.datetime = dt.datetime.fromtimestamp(Path(file_path).stat().st_ctime)
				nueva_clasificacion[file_path] = [
					self.docs[file_path][0],self.meses.get(file_date.month,None),file_date.year, Path(self.docs[file_path][0]).suffix
					]
			return nueva_clasificacion
		except Exception as e:
			ic(e)
			raise e

if __name__ == "__main__":
	clasificacion:object|Clasify_F = Clasify_F()
	print(clasificacion.clasificar_tipo_fecha())



