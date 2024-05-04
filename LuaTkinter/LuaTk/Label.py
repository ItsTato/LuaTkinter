from tkinter import ttk

from .Element import Element
from .PxDim import PxDim

from ..Console import Message, Tags

class Label(Element):
	def __init__(self,parent:Element|None) -> None:
		super().__init__()
		self.Name = "Label"

		self.__Tk = ttk.Label()

		self.__parent:Element|None=parent
		if parent is not None: self.Parent = parent
		self.__text:str=""
		self.__position:PxDim=PxDim(0,0)

		self.Text = "Blank label"

		return
	
	@property
	def TkCls(self) -> ttk.Label: return self.__Tk

	def __update_text(self) -> None: self.__Tk.config(text=self.__text)
	def __update_position(self) -> None: self.__Tk.place(x=self.__position.X,y=self.__position.Y)

	@property
	def Parent(self) -> Element|None:
		return self.__parent
	@Parent.setter
	def Parent(self,new_parent:Element|None) -> None:
		self.__parent = new_parent
		if isinstance(new_parent,Element): self.__Tk.master = new_parent.TkCls#; self.__Tk.pack()

	@property
	def Text(self) -> str:
		return self.__text
	@Text.setter
	def Text(self,new_value:str) -> None:
		self.__text = new_value
		self.__update_text()

	@property
	def Position(self) -> PxDim:
		return self.__position
	@Position.setter
	def Position(self,new_position:PxDim) -> None:
		self.__position = new_position
		self.__update_position()
