from typing import Any, Callable

class Element:
	def __init__(self) -> None:
		self.__name:str

	@property
	def Name(self) -> str:
		return self.__name
	@Name.setter
	def Name(self,new_name) -> None:
		self.__name = new_name
	
	@property
	def TkCls(self) -> Any:
		return
	
	def Bind(self,event:str,function:Callable) -> None:
		if self.TkCls is None: raise Exception("Element is missing a TkCls property.")
		match event:
			case "MouseButton1Click":
				self.TkCls.bind("<Button-1>",function)
				self.TkCls.bind("<Return>",function)
			case "MouseButton2Click":
				self.TkCls.bind("<Button-3>",function)
			case "MouseButton3Click":
				self.TkCls.bind("<Button-2>",function)
		return
	