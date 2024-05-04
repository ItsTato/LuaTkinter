from typing import Any, Callable

class Element:
	def __init__(self) -> None:
		self.__name:str
		self.__binds:dict[str,list[str]] = {
			"MouseButton1Click": ["Button-1","Return"],
			"MouseButton2Click": ["Button-3"],
			"MouseScrollWheelClick": ["Button-2"]
		}

	@property
	def Name(self) -> str:
		return self.__name
	@Name.setter
	def Name(self,new_name) -> None:
		self.__name = new_name
	
	@property
	def Binds(self) -> dict[str,list[str]]:
		return self.__binds
	@Binds.setter
	def Binds(self,new_binds:dict[str,list[str]]) -> None:
		self.__binds = new_binds
	def addBind(self,new_bind:str,binds:list[str]) -> None:
		self.__binds[new_bind] = binds
	
	@property
	def TkCls(self) -> Any:
		return
	
	def Bind(self,event:str,function:Callable) -> None:
		if self.TkCls is None: raise Exception("Element is missing a TkCls property.")
		if not event in self.__binds: raise Exception("Elemenet has no such bind.")
		for bind in self.__binds[event]: self.TkCls.bind(f"<{bind}>",function)
		return
	