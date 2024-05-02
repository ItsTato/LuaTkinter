class RGB:
	__cannot_exceed:str = "RGB values cannot exceed 255!"

	def __init__(self,red:int,green:int,blue:int) -> None:
		assert red <= 255, self.__cannot_exceed
		assert green <= 255, self.__cannot_exceed
		assert blue <= 255, self.__cannot_exceed

		self.__red:int = red
		self.__green:int = green
		self.__blue:int = blue

		return
	
	@property
	def Red(self) -> int:
		return self.__red
	@Red.setter
	def Red(self,new_value:int) -> None:
		assert new_value <= 255, self.__cannot_exceed
		self.__red = new_value
		return
	
	@property
	def Blue(self) -> int:
		return self.__blue
	@Blue.setter
	def Blue(self,new_value:int) -> None:
		assert new_value <= 255, self.__cannot_exceed
		self.__blue = new_value
		return
	
	@property
	def Green(self) -> int:
		return self.__green
	@Green.setter
	def Green(self,new_value:int) -> None:
		assert new_value <= 255, self.__cannot_exceed
		self.__green = new_value
		return
