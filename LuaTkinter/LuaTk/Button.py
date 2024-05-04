from tkinter import ttk
from typing import Callable

from .Element import Element
from .PxDim import PxDim

class Button(Element):
	def __init__(self,parent:Element|None) -> None:
		super().__init__()
		self.Name = "Button"

		self.__Tk:ttk.Button = ttk.Button()

		self.__parent:Element|None=parent
		if parent is not None: self.Parent = parent
		self.__text:str=""
		self.__position:PxDim=PxDim(0,0)

		self.Text = "New Button"

		return
	
	@property
	def TkCls(self) -> ttk.Button: return self.__Tk

	def __update_text(self) -> None: self.__Tk.config(text=self.__text)
	def __update_position(self) -> None: self.__Tk.place(x=self.__position.X,y=self.__position.Y)

	@property
	def Parent(self) -> Element|None:
		return self.__parent
	@Parent.setter
	def Parent(self,new_parent:Element|None) -> None:
		self.__parent = new_parent
		if isinstance(new_parent,Element): self.__Tk.master = new_parent.TkCls

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
	
	def Bind(self,event:str,function:Callable) -> None:
		match event:
			case "MouseButton1Click":
				self.__Tk.bind("<Button-1>",function)
				self.__Tk.bind("<Return>",function)
			case "MouseButton2Click":
				self.__Tk.bind("<Button-3>",function)
			case "MouseButton3Click":
				self.__Tk.bind("<Button-2>",function)
		return
