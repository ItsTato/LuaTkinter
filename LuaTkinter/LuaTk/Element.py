from typing import Any

class Element:
	def __init__(self,parent:"Element|None"=None) -> None:
		self.__name:str

		return

	@property
	def Name(self) -> str:
		return self.__name
	@Name.setter
	def Name(self,new_name) -> None:
		self.__name = new_name
	
	@property
	def TkCls(self) -> Any:
		return
	