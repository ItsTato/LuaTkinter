# This class has been commented extensively to serve as a starter
# point for people creating their own classes.

from tkinter import Tk
from typing import Callable

from .Element import Element
from .PxDim import PxDim

class Window(Element):
	def __init__(self,_:None) -> None:
		super().__init__()
		self.Name = "Window" # Assign default Name property.

		# Initialize Tkinter Object.
		self.__Tk:Tk = Tk()

		# Initialize all variables needed.
		# No default values are to be defined here.
		self.__title:str=""
		self.__size:PxDim=PxDim(0,0)
		self.__min_size:PxDim=PxDim(0,0)
		self.__max_size:PxDim=PxDim(0,0)
		self.__on_close:Callable=lambda: None
		self.__has_toolbar:bool=True
		self.__width_resizable:bool=True
		self.__height_resizable:bool=True

		# All default values are to be set here,
		# using the class's own properties.
		self.Title = "Lua Tkinter Window"
		self.Size = PxDim(400,300)
	
	@property
	def TkCls(self) -> Tk: return self.__Tk
	
	# Methods that interface with the Tkinter class.
	def __update_toolbar(self) -> None: self.__Tk.overrideredirect(not self.__has_toolbar)
	def __update_geometry(self) -> None: self.__Tk.geometry(f"{self.__size.X}x{self.__size.Y}")
	def __update_min_size(self) -> None: self.__Tk.minsize(self.__min_size.X,self.__min_size.Y)
	def __update_max_size(self) -> None: self.__Tk.maxsize(self.__max_size.X,self.__max_size.Y)
	def __update_resizable(self) -> None: self.__Tk.resizable(width=self.__width_resizable,height=self.__height_resizable)

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

	@property
	def HasToolbar(self) -> bool:
		return self.__has_toolbar
	@HasToolbar.setter
	def HasToolbar(self,new_value:bool) -> None:
		self.__has_toolbar = new_value
		self.__update_toolbar()
	
	@property
	def onClose(self) -> Callable:
		return self.__on_close
	@onClose.setter
	def onClose(self,function:Callable) -> None:
		self.__on_close = function
		self.__Tk.protocol("WM_DELETE_WINDOW",function)
	
	@property
	def WidthResizable(self) -> bool:
		return self.__width_resizable
	@WidthResizable.setter
	def WidthResizable(self,new_value:bool) -> None:
		self.__width_resizable = new_value
		self.__update_resizable()
	
	@property
	def HeightResizable(self) -> bool:
		return self.__height_resizable
	@HeightResizable.setter
	def HeightResizable(self,new_value:bool) -> None:
		self.__height_resizable = new_value
		self.__update_resizable()

	def Start(self) -> None:
		self.__Tk.mainloop()
	
	def Destroy(self) -> None:
		self.__Tk.destroy()
		del self
