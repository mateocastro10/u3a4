from coleccioncalefactores import ColeccionCalefactores
if __name__=='__main__':
    dimension=int(input('Ingrese cantidad de calefactores a gas a almacenar:'))
    dimensione=int(input('Ingrese cantidad de calefactores electricos a almacenar:'))
    manejacalefactores=ColeccionCalefactores(dimension,dimensione)
    manejacalefactores.LeerArchivos()
    gas=manejacalefactores.actividad1()
    ele=manejacalefactores.actividad2()
    manejacalefactores.actividad3(gas,ele)
