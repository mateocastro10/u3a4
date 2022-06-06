class Calefactor:
    __marca=''
    __modelo=''
    def __init__(self,marca,modelo,potencia,matricula,calorias):
        self.__marca=marca
        self.__modelo=modelo
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
