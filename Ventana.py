from Coordenada import Coordenada
class Ventana():
    __titulo=""
    __esquinaizq=Coordenada()
    __esquinader=Coordenada()
    def __init__(self,titulo="",Xizq=0,Yizq=0,Xder=500,Yder=500):
        self.__titulo=titulo
        self.__esquinaizq.setXY(Xizq,Yizq)
        self.__esquinader.setXY(Xder,Yder)
    def alto(self):
        return self.__esquinader.y()-self.__esquinaizq.y()
    def ancho(self):
        return self.__esquinader.x()-self.__esquinaizq.x()
    def gettitulo(self):
        return self.__titulo