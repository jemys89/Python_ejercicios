from obtenerLetraDni import *
from accesoDatos import *
#def crearFicheroDNI(ficheroDni, matrizNumerosDNI)


if __name__ == "__main__":
    rutaAccesoFichero = "./test.gr"

    matrizNumerosDni = []
    matrizNumerosDni = accesoCasosTest(matrizNumerosDni, rutaAccesoFichero)
    matrizDNI = []
    for numero in matrizNumerosDni:        
        matrizDNI.append(obtenerLetraDni(numero))
    print (matrizDNI)        
