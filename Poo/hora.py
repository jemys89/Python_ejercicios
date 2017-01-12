#Construye una clase de nombre Hora que permita almacenar la hora, así como los métodos para manipularla
# (este es nuestro ADT). Tendrá las siguientes propiedades y métodos:
#Propiedades (todas ellas privadas):
#hora: de tipo entero (00 - 24)
#minutos: de tipo entero (00 - 59)
#segundos: de tipo entero (00 - 59)
#Constructor (inicializador en Python):
#Constructor que, por defecto, inicialice las propiedades de la clase a 0 [programación defensiva].
#Constructor al que se le pasen como argumentos tres enteros y se los asigne a las propiedades de la clase.
# Si la cantidad recibida no satisface las restricciones de los valores impuestos a horas, minutos y segundos,
# el valor que se fija es 0 [Manejo de errores]: devolver un valor neutro, aunque en este caso no lo sea.
#Métodos de la clase (públicos):
#setHora(): recibe como argumentos tres enteros y se los asigna a las propiedades de la clase. Utiliza el mismo nombre
# en las variables que reciben los argumentos y en las propiedades de la clase. Este método ha de diseñarse mediante
# programación por contrato, es decir, debe incluir una precondición: si los valores recibidos no satisfacen 
#las restricciones de los valores impuestos a horas, minutos y segundos, el valor que se establece es 0 
#[Manejo de errores: devolver un valor neutro, aunque en este caso no lo sea]. Ya que va a ser utilizado en el cosntructor,
# este precondición podría implementarse en su propia rutina para ser llamada desde este método y desde el “constructor”.
#getHora(): devuelve la hora como una lista de la forma [horas, minutos, segundos] o como un string de la 
#forma "horas:minutos:segundos".
#imprmirHora() que muestra en consola la hora en formato string de la forma "horas:minutos:segundos".
#Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].

### Defino la clase "Hora"###
class Hora:
	def __init__(self,hora,minutos,segundos):
		if hora>24 or hora <0:
			self.__hora = 0
		else:
			self.__hora = hora
		if minutos>=60 or minutos<0:
			self.__minutos = 0
		else:
			self.__minutos = minutos
		if segundos>=60 or segundos<0:
			self.__segundos = 0
		else:
			self.__segundos = segundos

	### Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].  ###
	def setHora(self, hora, minutos, segundos):
		self.__hora = hora
		self.__minutos = minutos
		self.__segundos = segundos

	def setMinutos(self, minutos):
		self.__minutos = minutos

	def setSegundos(self, segundos):
		self.__segundos = segundos

	def getHora(self):
		return print((self.__hora),":",(self.__minutos),":",self.__segundos)

	def getMinutos(self):
		return self.__minutos

	def getSegundos(self):
		return self.__segundos

	### imprmirHora() que muestra en consola la hora en formato string de la forma "horas:minutos:segundos".  ###
	def imprimirHora(self):
		return print((self.__hora),":",(self.__minutos),":",self.__segundos)

######  Casos Test   #####
tiempo = Hora(15,45,15)
tiempo.getHora()
lluvia = Hora(25,45,26)
lluvia.getHora()



	


		