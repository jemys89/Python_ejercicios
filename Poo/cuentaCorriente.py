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
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.direccion = ""
        self.telefono = ""
        self.nif = ""
        self.saldo = 0

    ###Métodos públicos "set()"
    def setNombre(self, nombre):
        self.nombre = nombre


    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setDni(self, nif):
        self.nif = nif

    def setSaldo(self, saldo):
        self.saldo = saldo

    ###Métodos públicos "get()"
    def getNombre(self, nombre):
        return self.nombre

    def getApellidos(self, apellidos):
        return self.apellidos

    def getDireccion(self, direccion):
        return self.direccion

    def getDni(self, nif):
        return self.nif

    def getSaldo(self, saldo):
        return self.saldo

    ### retirarDinero(): resta al saldo una cantidad de dinero pasada como argumento. ###
    def retirarDinero(self, saldo):
        try:
            self.saldo = self.saldo - saldo
        except TypeError:
            print("El valor introducido no és de tipo númerico")

    ### ingresarDinero(): añade al saldo una cantidad de dinero.###
    def ingresarDinero(self, saldo):
        try:
            self.saldo = self.saldo + saldo
        except TypeError:
            print("El valor introducido no és de tipo númerico")

    ### consultarCuenta(): visualizará los datos de la cuenta.###
    def consultarCuenta(self,):
        print("Nombre: {}".format(self.nombre))
        print("Apellidos: {}".format(self.apellidos))
        print("Dirección: {}".format(self.direccion))
        print("Teléfono: {}".format(self.telefono))
        print("NIF: {}".format(self.nif))
        print("Saldo: {}.".format(self.saldo))

    ### saldoNegativo(): devolverá un valor lógico indicando si la cuenta está o no en números rojos.###
    def saldoNegativo(self, saldo):
        if self.saldo - self.saldo == 0:
            return True
        else:
            return False


############  Casos Test  ###############
if __name__ == '__main__':

    # Definimos un objeto llamado "usuario"
    usuario = CuentaCorriente()
    usuario.setDni("4219586Q")
    usuario.setNombre("Pulgarcito")
    usuario.setApellidos("Buscaba un garbancito")
    usuario.setDireccion("En una calle llena de niebla")
    usuario.setTelefono("699354876")
    usuario.setSaldo(6500.0)

    usuario.consultarCuenta()
    usuario.ingresarDinero(200)
    usuario.consultarCuenta()
    usuario.retirarDinero(400)
    usuario.consultarCuenta()
    if usuario.saldoNegativo == True:
        print("Saldo negativo: Estás seco...")
    else:
        print("Saldo negativo:  Aún sobrevives... quedan monedas en tu cuenta")

















