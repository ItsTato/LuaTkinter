from tkinter import Tk
from typing import Any

from .Element import Element

class Window(Element):
	def __init__(self,_:None) -> None:
		super().__init__(None)
		self.Name = "Window" # Assign default Name property.

		# Initialize Tkinter Object.
		self.__Tk:Tk = Tk()

		# Initialize all variables needed.
		# No default values are to be defined here.
		self.__title:str=""
		self.__width:int=0
		self.__height:int=0
		self.__min_width:int|None=None
		self.__min_height:int|None=None
		self.__max_width:int|None=None
		self.__max_height:int|None=None

		# All default values are to be set here,
		# using the class's own properties.
		self.Title = "Lua Tkinter Window"
		self.Width = 400
		self.Height = 300
	
	@property
	def TkCls(self) -> Any: return self.__Tk
	
	def __update_geometry(self) -> None: self.__Tk.geometry(f"{self.__width}x{self.__height}")
	def __update_min_size(self) -> None: self.__Tk.minsize(self.__min_width if isinstance(self.__min_width,int) else 0,self.__min_height if isinstance(self.__min_height,int) else 0)
	def __update_max_size(self) -> None: self.__Tk.maxsize(self.__max_width if isinstance(self.__max_width,int) else 0,self.__max_height if isinstance(self.__max_height,int) else 0)
	
	@property
	def Title(self) -> str:
		return self.__title
	@Title.setter
	def Title(self,new_title:str) -> None:
		self.__title = new_title
		self.__Tk.title(new_title)

	@property
	def Width(self) -> int:
		return self.__width
	@Width.setter
	def Width(self,new_width) -> None:
		self.__width = new_width
		self.__update_geometry()
	
	@property
	def Height(self) -> int:
		return self.__height
	@Height.setter
	def Height(self,new_height) -> None:
		self.__height = new_height
		self.__update_geometry()
	
	@property
	def MinWidth(self) -> int|None:
		return self.__min_width
	@MinWidth.setter
	def MinWidth(self,new_value:int|None) -> None:
		self.__min_width = new_value
		self.__update_min_size()
	
	@property
	def MinHeight(self) -> int|None:
		return self.__min_height
	@MinHeight.setter
	def MinHeight(self,new_value:int|None) -> None:
		self.__min_height = new_value
		self.__update_min_size()

	@property
	def MaxWidth(self) -> int|None:
		return self.__max_width
	@MaxWidth.setter
	def MaxWidth(self,new_value:int|None) -> None:
		self.__max_width = new_value
		self.__update_max_size()

	@property
	def MaxHeight(self) -> int|None:
		return self.__max_height
	@MaxHeight.setter
	def MaxHeight(self,new_value:int|None) -> None:
		self.__max_height = new_value
		self.__update_max_size()

	def run(self) -> None:
		self.__Tk.mainloop()
