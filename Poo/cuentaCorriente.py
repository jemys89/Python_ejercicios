#Cuenta Corriente
#Construye una clase de nombre CuentaCorriente que permita almacenar los datos asociados a la cuenta bancaria de un cliente,
# e interactuar con ellos. Este es nuestro ADT.
#Esta clase tendrá las siguientes propiedades, métodos y constructores:
#Propiedades privadas (de momento, en Python nos da igual que sean privadas): 
#nombre, apellidos, dirección, teléfono: todas de tipo string.
#NIF: objeto instancia de la clase DNI que resolvimos en clase**. Se trata de una relación “Has-A” o “Tiene-una”.
#saldo: de tipo double.
#Constructores (inicializador en Python): 
#Constructor que por defecto inicializa las propiedades de la clase (programación defensiva).
#Constructor al que se le pasen como argumentos todas las propiedades que tiene la clase.
#Métodos públicos: 
#set() y get() para todas las propiedades de la clase [Abstracción y encapsulamiento].
#retirarDinero(): resta al saldo una cantidad de dinero pasada como argumento.
#ingresarDinero(): añade al saldo una cantidad de dinero.
#consultarCuenta(): visualizará los datos de la cuenta.
#saldoNegativo(): devolverá un valor lógico indicando si la cuenta está o no en números rojos.
#** Puedes reutilizar la clase DNI que construimos en clase para definir la clase NIF mediante [herencia], si es que fuese 
#necesario alguna especialización o cambio en la clase DNI. Evalúa si es posible reutilizarla tal cual.

###Clase cuenta corriente###
class CuentaCorriente:
    ###Inicialización de las propiedades privadas###
    def __init__(self,nombre,apellidos,direccion,telefono,nif,saldo=0):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefono = telefono
        self.__nif = nif
        self.__saldo = saldo

    ###Métodos públicos "set()"
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setNif(self, nif):
        self.__nif = nif

    def setSaldo(self, saldo):
        self.__saldo = saldo

    ###Métodos privados "get()"
    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def getDireccion(self):
        return self.__direccion

    def getNif(self):
        return self.__nif

    def getSaldo(self):
        return self.__saldo

    ### retirarDinero(): resta al saldo una cantidad de dinero pasada como argumento. ###
    def retirarDinero(self, adeudo):
        try:
            self.__saldo = self.__saldo - adeudo
        except TypeError:
            print("El valor introducido no és de tipo númerico")

    ### ingresarDinero(): añade al saldo una cantidad de dinero.###
    def ingresarDinero(self, ingreso):
        try:
            self.__saldo = self.__saldo + ingreso
        except TypeError:
            print("El valor introducido no és de tipo númerico")

    ### consultarCuenta(): visualizará los datos de la cuenta.###
    def consultarCuenta(self):
        print("Nombre: {}".format(self.__nombre))
        print("Apellidos: {}".format(self.__apellidos))
        print("Dirección: {}".format(self.__direccion))
        print("Teléfono: {}".format(self.__telefono))
        print("NIF: {}".format(self.__nif))
        print("Saldo: {}.".format(self.__saldo))

    ### saldoNegativo(): devolverá un valor lógico indicando si la cuenta está o no en números rojos.###
    def saldoNegativo(self):
        if self.__saldo < 0:
            return True
        else:
            return False


############  Casos Test  ###############
if __name__ == '__main__':

    # Definimos un objeto llamado "usuario"
    usuario = CuentaCorriente("Jamal","Mohamet","C/Pulgarcito nº2","666 666 666","43000000A",6500.0)
   
    print(usuario.getNombre())
    usuario.setNombre("Marc")
    print(usuario.getNombre())
    print(usuario.getSaldo())
    usuario.ingresarDinero(1100)
    print(usuario.getSaldo())
    usuario.retirarDinero(10000)
    print(usuario.saldoNegativo())
    print(usuario.consultarCuenta())


  














