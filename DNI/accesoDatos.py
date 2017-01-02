from obtenerLetraDni import*

def accesoCasosTest(matrizCasosTest, rutaAccesoFichero):
    """
    Accede al fichero y devuelve el conjunto de numeros de DNIs en una matriz .
    """
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print ("Fichero no encontrado")
        return []
    except ValueError:
        print ("El contenido del fichero ha de ser uns string")
    else:
        matrizCasosTest = []
        for linea in fichero:
            item = linea.rstrip()
            matrizCasosTest.append(item)
        return matrizCasosTest
    
def mostrarCasosTest(matrizCasosTest):
    for numerosDni in matrizCasosTest:
        print (numerosDni)
    print (matrizCasosTest)




if __name__ == "__main__":
    rutaAccesoFichero = "./casostest.txt"
    matrizCasosTest = []
    matrizCasosTest = accesoCasosTest(matrizCasosTest, rutaAccesoFichero)
    mostrarCasosTest(matrizCasosTest)