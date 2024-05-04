class PixDim:
    def __init__(self,x:int,y:int) -> None:
        self.__x:int = x
        self.__y:int = y
        return
    
    def new(x:int,y:int) -> "PixDim": # type: ignore
        return PixDim(x,y)
    
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
