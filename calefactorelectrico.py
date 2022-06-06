from calefactor import Calefactor


class CalefactorElectrico(Calefactor):
    __potencia=''
    def __init__(self,marca,modelo,potencia,matricula='',calorias=''):
        super().__init__(marca,modelo,potencia,matricula,calorias)
        self.__potencia=potencia
    def getMarca(self):
        return super().getMarca()
    def getModelo(self):
        return super().getModelo()
    def getPotencia(self):
        return self.__potencia
