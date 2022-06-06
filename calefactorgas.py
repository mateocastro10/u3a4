from calefactor import Calefactor


class CalefactorGas(Calefactor):
    __matricula=''
    __calorias=0
    def __init__(self,marca,modelo,potencia='', matricula='',calorias=0):
        super().__init__(marca,modelo,potencia,matricula,calorias)
        self.__matricula=matricula
        self.__calorias=calorias
    def getCalorias(self):
        return self.__calorias
    def getModelo(self):
        return super().getModelo()
    def getMarca(self):
        return super().getMarca()
