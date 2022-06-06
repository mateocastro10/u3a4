import numpy as np
import csv
from calefactorelectrico import CalefactorElectrico
from calefactorgas import CalefactorGas
class ColeccionCalefactores:
    __cantidade=0
    __cantidadg=0
    def __init__(self,dimension=2,dimensione=4):
        self.__calefactoresele=np.empty(dimensione,dtype=CalefactorElectrico)
        self.__calefactoresgas=np.empty(dimension,dtype=CalefactorGas)
    def agregarg(self,calefactor):
        self.__calefactoresgas[self.__cantidadg]=calefactor
        self.__cantidadg+=1
    def agregare(self,calefactor):
        self.__calefactoresele[self.__cantidade]=calefactor
        self.__cantidade+=1
    def LeerArchivos(self):
        band=True
        archivog=open('calefactor-a-gas.csv')
        reader=csv.reader(archivog,delimiter=',')
        for fila in reader:
            if(band):
                band=False
            else:
                calefactor=CalefactorGas(fila[0],fila[1],'',fila[2],int(fila[3]))
                self.agregarg(calefactor)
        archivog.close()
        archivoe=open('calefactor-electrico.csv')
        reader=csv.reader(archivoe,delimiter=',')
        for fila in reader:
            if(not band):
                band=True
            else:
                calefactor=CalefactorElectrico(fila[0],fila[1],int(fila[2]))
                self.agregare(calefactor)
        archivoe.close()
        print('Archivos leidos con exito!')
    def actividad1(self):
        print('--------MENOR CONSUMO GAS---------')
        min=999999
        costo=input('Ingresar costo por metro cubico:')
        cantidad=input('cantidad que se espera consumir:')
        for i in self.__calefactoresgas:
            if(min>i.getCalorias()):
                min=i.getCalorias()
                calefactor=i
        print('marca:{} modelo:{}'.format(calefactor.getMarca(),calefactor.getModelo()))
        return calefactor
    def actividad2(self):
        print('--------MENOR CONSUMO ELECTRICO---------')
        min=999999
        costo=input('Ingresar costo por kilowatt/h:')
        cantidad=input('cantidad que se espera consumir:')
        for i in self.__calefactoresele:
            if(min>i.getPotencia()):
                min=i.getPotencia()
                calefactor=i
        print('marca:{} modelo:{}'.format(calefactor.getMarca(),calefactor.getModelo()))
        return calefactor
    def actividad3(self,gas,ele):
        print('--------MENOR CONSUMO---------')
        if(gas.getCalorias()<ele.getPotencia()):
            print('modelo:{} marca:{} matricula:{} calorias:{}'.format(gas.getModelo(),gas.getMarca(),gas.getMatricula(),gas.getCalorias()))
        else:
            print('modelo:{} marca:{} potencia:{}'.format(ele.getModelo(),ele.getMarca(),ele.getPotencia()))
