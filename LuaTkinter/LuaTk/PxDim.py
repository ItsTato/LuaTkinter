class PxDim:
	def __init__(self,x:int,y:int) -> None:
		self.__x:int = x
		self.__y:int = y
		return
	
	def __str__(self) -> str: return f"{self.__x}x{self.__y}"
	def __add__(self,other:"PxDim") -> "PxDim": return PxDim(self.X+other.X,self.Y+other.Y)
	
	def new(x:int,y:int) -> "PxDim": # type: ignore
		return PxDim(x,y)
	
	@property
	def X(self) -> int:
		return self.__x
	@X.setter
	def X(self,new_value:int) -> None:
		self.__x = new_value

	@property
	def Y(self) -> int:
		return self.__y
	@Y.setter
	def Y(self,new_value:int) -> None:
		self.__y = new_value

	@property
	def Tuple(self) -> tuple:
		return (self.__x,self.__y)

	@property
	def String(self) -> str:
		return self.__str__()
