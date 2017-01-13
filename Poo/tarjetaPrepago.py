#Construye una clase de nombre TarjetaPrepago que permita interactuar con la información almacenada en una tarjeta
# de telefonía móvil prepago (este es nuestro ADT).
#-Esta clase tendrá las siguientes propiedades, métodos y constructores:
#Propiedades privadas:
###-numeroTeléfono: de tipo string.
###-NIF: objeto instancia de la clase DNI que resolvimos en clase**. Se trata de una relación “Has-A” o “Tiene-una”
###-saldo: de tipo double (en euros).
###-consumo: objeto instancia de la clase Hora, para almacenar las horas, minutos y segundos consumidos.
### Se trata de otra relación “Has-A” o “Tiene-una”. Reutiliza la clase Hora que has construído en el ejercicio anterior.
#Constructores:
#Constructor que inicializa las propiedades de la clase (programación defensiva).
#Constructor que recibe como argumentos los valores para las propiedades de clase numeroTelefono, NIF y saldo.
#Métodos públicos:
###set() y get() para todas las propiedades de la clase [Abstracción y encapsulamiento].
###-ingresarSaldo(): añade al saldo una cantidad de dinero.
### -enviarMensaje(): recibe como argumento un entero que representa un número de mensajes a enviar,  ###
## y resta al saldo 9 céntimos por mensaje.
###-realizarLlamada(): recibe un entero que representa el número de segundos hablados. Se restará al saldo la cantidad
### correspondiente calculada en base a 15 céntimos por establecimiento de llamada y 1 céntimo por segundo.
#### También se actualizará la propiedad consumo.
###-consultarTarjeta(): visualizará todos los datos de la tarjeta en consola.
####Métodos privados.
#Necesitarás un método que se encargue de la responsabilidad de convertir la hora (hora:minutos:segundos)
# a segundos para poder sumar la duración de la llamada al total de la duración de las llamadas en la propiedad consumo.
#Haz uso de todos aquellos métodos privados que estimes necesarios.

### Construye una clase de nombre TarjetaPrepago que permita interactuar con la información almacenada en una tarjeta ###
from hora import*
class TarjetaPrepago:
	#Propiedades privadas:
	def __init__(self, numeroTelefono, nif, saldo = 0):
		self.__numeroTelefono = numeroTelefono
		self.__nif = nif
		self.__saldo = saldo
		self.__consumo = 0

	### set() y get() para todas las propiedades de la clase [Abstracción y encapsulamiento]. ###
	def setNumeroTelefono(self, numeroTelefono):
		self.__numeroTelefono = numeroTelefono

	def setNif(self, nif):
		self.__nif = nif

	def setSaldo(self, saldo):
		self.__saldo = saldo

	def setConsumo(self, hora, minutos, segundos):
		self.__consumo.setHora(hora, minutos, segundos)

	def getNumeroTelefono(self):
		return self.__numeroTelefono

	def getNif(self):
		return self.__nif

	def getSaldo(self):
		return self.__saldo

	def getConsumo(self):
		return self.__consumo.Hora()

	### -ingresarSaldo(): añade al saldo una cantidad de dinero. ###
	def ingresarSaldo(self, dinero):
		self.__saldo += dinero

	###enviarMensaje(): recibe como argumento un entero que representa un número de mensajes a enviar###
	def enviarMensaje(self, cantidadMensaje):
		precioMensaje=0.09
		self.__saldo = self.__saldo - (cantidadMensaje * precioMensaje)

	def realizarLlamada(self, segundos):
		establecimientoLLamada = 0.15
		self.__saldo -= establecimientoLLamada + segundos/100

	def consultarTarjeta(self):
		print("Número de teléfono: {}".format(self.__numeroTelefono))
		print("Nif: {}".format(self.__nif))
		print("Saldo: {}".format(self.__saldo))
		

if __name__ == '__main__':
	tarjeta = TarjetaPrepago("654878987","43125248Q",20)
	tarjeta.consultarTarjeta()
	tarjeta.enviarMensaje(4)
	tarjeta.consultarTarjeta()
	tarjeta.realizarLlamada(30)
	tarjeta.consultarTarjeta()
	tarjeta.ingresarSaldo(20)
	tarjeta.consultarTarjeta()