class Element:
	def __init__(self,parent:"Element|None"=None) -> None:
		self.__parent:Element|None = parent
		self.__children:list[Element] = []

		self.__name:str

		return
	
	@property
	def Parent(self) -> "Element|None":
		return self.__parent
	@Parent.setter
	def Parent(self,new_parent:"Element|None") -> None:
		if self.__parent is not None: self.__parent.remove_child_named(self.__name)
		self.__parent = new_parent

	@property
	def Name(self) -> str:
		return self.__name
	@Name.setter
	def Name(self,new_name) -> None:
		self.__name = new_name

	def add_child(self,child:"Element") -> None:
		self.__children.append(child)
		return
	def remove_child(self,child:"Element") -> None:
		for Element in self.__children:
			if Element.Name == child.Name:
				self.__children.remove(Element)
				break
		return
	def remove_child_named(self,child_name:str) -> None:
		for Element in self.__children:
			if Element.Name == child_name:
				self.__children.remove(Element)
				break
		return
	@property
	def children(self) -> list["Element"]:
		return self.__children