from tkinter import ttk
from typing import Any

from .Element import Element

class Label(Element):
	def __init__(self,parent:Element|None) -> None:
		super().__init__(parent)
		self.Name = "Label"
		self.__Tk = ttk.Label(parent.TkCls)
		self.__Tk.config(text="WOW")
		self.__Tk.pack()
	
	@property
	def TkCls(self) -> Any: return self.__Tk
	
