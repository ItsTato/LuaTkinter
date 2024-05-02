from .__RGB import RGB as RGB_Class

class Color:
	def __init__(self,red:int,green:int,blue:int) -> None:
		assert red <= 255, "RGB values cannot exceed 255!"
		assert green <= 255, "RGB values cannot exceed 255!"
		assert blue <= 255, "RGB values cannot exceed 255!"

		self.__RGB:RGB_Class = RGB_Class(red,green,blue)

		return
	
	def new(red:int,green:int,blue:int) -> "Color": # type: ignore
		return Color(red,green,blue)
	
	@property
	def RGB(self) -> RGB_Class:
		return self.__RGB
	
	@property
	def Hex(self) -> str:
		return f"#{self.__RGB.Red:02x}{self.__RGB.Green:02x}{self.__RGB.Blue:02x}"
