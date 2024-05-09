from tkinter import ttk

from .Element import Element
from .PxDim import PxDim

class Frame(Element):
	def __init__(self,parent:Element|None) -> None:
		super().__init__()
		self.Name = "Frame"

		self.__Tk:ttk.Frame = ttk.Frame()

		self.__parent:Element|None=parent
		if parent is not None: self.Parent = parent
		self.__position:PxDim=PxDim(0,0)
	
	@property
	def TkCls(self) -> ttk.Frame: return self.__Tk

	def __update_position(self) -> None: self.__Tk.place(x=self.__position.X,y=self.__position.Y)

	@property
	def Position(self) -> PxDim:
		return self.__position
	@Position.setter
	def Position(self,new_position:PxDim) -> None:
		self.__position = new_position
		self.__update_position()
