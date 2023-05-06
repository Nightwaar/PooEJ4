class Coordenada():
    __x=0
    __y=0
    def __init__(self,x=0,y=0):
        self.__x=int(x)
        self.__y=int(y)
        return
    def setX(self,x=0):
        self.__x=int(x)
        return
    def setY(self,y=0):
        self.__y=int(y)
        return
    def setXY(self,x=0,y=0):
        self.setX(x)
        self.setY(y)
        return
    def x(self):
        return self.__x
    def y(self):
        return self.__y