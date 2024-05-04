# This class has been commented extensively to serve as a starter
# point for people creating their own classes.

from tkinter import Tk
from typing import Any

from .Element import Element
from .PxDim import PxDim

class Window(Element):
	def __init__(self,_:None) -> None:
		super().__init__(None)
		self.Name = "Window" # Assign default Name property.

		# Initialize Tkinter Object.
		self.__Tk:Tk = Tk()

		# Initialize all variables needed.
		# No default values are to be defined here.
		self.__title:str=""
		self.__size:PxDim=PxDim(0,0)
		self.__min_size:PxDim=PxDim(0,0)
		self.__max_size:PxDim=PxDim(0,0)

		# All default values are to be set here,
		# using the class's own properties.
		self.Title = "Lua Tkinter Window"
		self.Size = PxDim(400,300)
	
	@property
	def TkCls(self) -> Any: return self.__Tk
	
	# Methods that interface with the Tkinter class.
	def __update_geometry(self) -> None: self.__Tk.geometry(f"{self.__size.X}x{self.__size.Y}")
	def __update_min_size(self) -> None: self.__Tk.minsize(self.__min_size.X,self.__min_size.Y)
	def __update_max_size(self) -> None: self.__Tk.maxsize(self.__max_size.X,self.__max_size.Y)
	
	@property
	def Title(self) -> str:
		return self.__title
	@Title.setter
	def Title(self,new_title:str) -> None:
		self.__title = new_title
		self.__Tk.title(new_title)

	@property
	def Size(self) -> PxDim:
		return self.__size
	@Size.setter
	def Size(self,new_size:PxDim) -> None:
		self.__size = new_size
		self.__update_geometry()
	
	@property
	def MinSize(self) -> PxDim:
		return self.__min_size
	@MinSize.setter
	def MinSize(self,new_size:PxDim) -> None:
		self.__min_size = new_size
		self.__update_min_size()

	@property
	def MaxSize(self) -> PxDim:
		return self.__max_size
	@MaxSize.setter
	def MaxSize(self,new_size:PxDim) -> None:
		self.__max_size = new_size
		self.__update_max_size()

	def run(self) -> None:
		self.__Tk.mainloop()
